from flask import jsonify
from conexao import Conexao
from datetime import datetime
from model import Titulo, LogRetornoBancario
from utils import Utils


class TituloDAO(object):

    def obter(self, numero_documento, cod_empresa):
        conexao = Conexao()
        registro = conexao.consultar('SELECT v.cod_titulo, v.numero_documento_sicredi, v.valor_titulo, \
        v.numero_contrato, v.status, v.valor_titulo_liquido, v.data_pagamento, v.tipo_titulo, \
        v.cod_plano_empresa, v.data_vencimento, v.numero_ordem_servico \
        FROM public.vw_listar_titulos_retorno_bancario v \
        WHERE v.cod_empresa = %s \
        AND v.numero_documento_sicredi = %s' % (cod_empresa, numero_documento))

        if registro is not None:
            return Titulo(cod_titulo=registro[0], numero_documento=registro[1],
                          valor_titulo=float(registro[2]), numero_contrato=registro[3], status=registro[4],
                          valor_titulo_liquido=float(registro[5]), data_pagamento=registro[6],
                          tipo_titulo=registro[7], cod_plano_empresa=registro[8],
                          data_vencimento=registro[9].isoformat(), numero_os=registro[10])
        else:
            return None

    def listar(self, tupla_numeros_documentos, cod_empresa):
        titulos = []
        conexao = Conexao()
        registros = conexao.listar('SELECT v.cod_titulo, v.numero_documento_sicredi, v.valor_titulo, \
        v.numero_contrato, v.status, v.valor_titulo_liquido, v.data_pagamento, v.tipo_titulo, \
        v.cod_plano_empresa, v.data_vencimento, v.numero_ordem_servico \
        FROM public.vw_listar_titulos_retorno_bancario v \
        WHERE v.cod_empresa = %s \
        AND v.numero_documento_sicredi IN %s' % (cod_empresa, tupla_numeros_documentos))
        if registros is not None:
            for registro in registros:
                titulos.append(Titulo(cod_titulo=registro[0], numero_documento=registro[1],
                                      valor_titulo=float(registro[2]), numero_contrato=registro[3], status=registro[4],
                                      valor_titulo_liquido=float(registro[5]),
                                      data_pagamento=Utils.formatar_data_json(registro[6].isoformat()) if registro[6] is not None else None,
                                      tipo_titulo=registro[7], cod_plano_empresa=registro[8],
                                      data_vencimento=Utils.formatar_data_json(registro[9].isoformat()),
                                      numero_os=registro[10]).to_dict())

        return titulos

    def listar_numero_documento_sicredi(self):
        conexao = Conexao()
        registros = conexao.listar('SELECT numero_documento_sicredi \
        FROM public.vw_listar_titulos_retorno_bancario \
        WHERE cod_empresa = 2 \
        ORDER BY 1 \
        LIMIT 1140')
        return registros


class NumeroDAO(object):

    @staticmethod
    def gerar_id(cod_empresa, classe):
        conexao = Conexao()
        registro = conexao.consultar("SELECT public.fn_nextval({}, '{}', 1)".format(cod_empresa, classe))
        return long(registro[0])


class LogRetornoBancarioDAO(object):

    @staticmethod
    def salvar(log_retorno_bancario):
        query = '''INSERT INTO public.erp_log_retorno_bancario 
        (cod_log_retorno_bancario, cod_empresa, motivo, numero_documento, numero_linha, status, valor_pago, 
        data_processamento, data_insert   
        '''
        values = "VALUES ({}, {}, '{}', {}, {}, '{}', {}, '{}', now()"
        if log_retorno_bancario.cod_titulo is not None:
            query + ', cod_titulo)'
            values + ', {})'
        else:
            query + ')'
            values + ')'
        query_completa = query + values
        conexao = Conexao()
        conexao.executar(query_completa.format(log_retorno_bancario.codigo, log_retorno_bancario.cod_empresa,
                                               log_retorno_bancario.motivo, log_retorno_bancario.numero_documento,
                                               log_retorno_bancario.numero_linha, log_retorno_bancario.status,
                                               log_retorno_bancario.valor_pago, log_retorno_bancario.data_processamento,
                                               log_retorno_bancario.cod_titulo))
