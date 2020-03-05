from registro import Registro
from dao import TituloDAO, LogRetornoBancarioDAO, NumeroDAO
from datetime import datetime
from flask import request, jsonify
from model import LogRetornoBancario
import tempfile


class RetornoService(object):

    def processar_arquivo(self, nome_arquivo):
        '''
        o que deve ser feito
        1 - tratar descricao das ocorrencias
        3 - tratar descricao das inconsistencias
        '''
        cod_empresa = int(request.args.get('cod_empresa'))
        with open(tempfile.gettempdir() + nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
        registros = []
        cont = 0
        titulo_dao = TituloDAO()
        for linha in linhas:
            cont = cont + 1
            if linha[0] == '1':
                numero_documento = linha[47:62].strip()
                numero_documento = numero_documento[0:len(numero_documento)-1]
                if linha[13] == 'A':
                    valor_pago = linha[253:266]
                    tarifa = linha[175:188]
                elif linha[13] == 'C':
                    valor_pago = linha[152:165]
                    tarifa = linha[152:165]
                tarifa = 0 if tarifa is None else tarifa
                registros.append(Registro(linha=cont, numero_documento=numero_documento, ocorrencia=linha[108:110],
                                          data_pagamento=linha[110:116], subocorrencias=linha[318:328],
                                          valor_pago=valor_pago, tarifa=tarifa).to_dict())
        numeros_documentos = tuple(sorted([r.get('numero_documento') for r in registros]))
        titulos = titulo_dao.listar(numeros_documentos, cod_empresa)
        map_titulos = {}
        for titulo in titulos:
            map_titulos[str(titulo.get('numeroDocumento'))] = titulo
        for registro in registros:
            if registro.get('numero_documento') in map_titulos:
                registro['titulo'] = map_titulos[registro.get('numero_documento')]

        for registro in registros:
            motivo = ''
            if registro.get('inconsistente'):
                motivo = 'DI'
            elif registro.get('titulo') is None:
                motivo = 'TI'
            elif registro.get('titulo').get('status') == 'I':
                motivo = 'TIN'
            if motivo != '':
                log_retorno = LogRetornoBancario(codigo=NumeroDAO.gerar_id(cod_empresa, 'LogRetornoBancario'),
                                                 cod_empresa=cod_empresa, motivo=motivo,
                                                 numero_documento=registro.get('numero_documento'),
                                                 numero_linha=registro.get('linha'), valor_pago=registro.get('valor_pago'),
                                                 data_processamento=registro.get('data_pagamento'), status='P')
                LogRetornoBancarioDAO.salvar(log_retorno)
            if registro.get('ocorrencia') in ['06', '07', '08'] and registro.get('titulo') is not None:
                log_retorno = LogRetornoBancario(codigo=NumeroDAO.gerar_id(cod_empresa, 'LogRetornoBancario'),
                                                 cod_empresa=cod_empresa, motivo='',
                                                 cod_titulo=registro.get('titulo').get('codTitulo'),
                                                 numero_documento=registro.get('numero_documento'),
                                                 numero_linha=registro.get('linha'),
                                                 valor_pago=registro.get('valor_pago'),
                                                 data_processamento=registro.get('data_pagamento'), status='BA')
                LogRetornoBancarioDAO.salvar(log_retorno)

        return registros


class TituloService(object):

    def consultar_titulo(self, numero_documento, cod_empresa):
        return TituloDAO().obter(numero_documento, cod_empresa)
