class Titulo(object):

    def __init__(self, cod_titulo, numero_documento, numero_contrato, valor_titulo, status, valor_titulo_liquido, data_pagamento, tipo_titulo, cod_plano_empresa, data_vencimento, numero_os):
        self.codTitulo = cod_titulo
        self.numeroDocumento = numero_documento
        self.valorTitulo = valor_titulo
        self.status = status
        self.valorTituloLiquido = valor_titulo_liquido
        self.tipoTitulo = tipo_titulo
        self.codPlanoEmpresa = cod_plano_empresa
        self.dataVencimento = data_vencimento
        self.dataPagamento = data_pagamento
        if numero_contrato is not None:
            self.contrato = {'numeroContrato': numero_contrato}
        if numero_os is not None:
            self.ordemServico = {'numeroOrdemServico': numero_os}

    def to_dict(self):
        return self.__dict__


class LogRetornoBancario(object):

    def __init__(self, codigo, cod_empresa, motivo, numero_documento, numero_linha, valor_pago, data_processamento,
                 status, cod_titulo):
        self.codigo = codigo
        self.cod_empresa = cod_empresa
        self.motivo = motivo
        self.numero_documento = numero_documento
        self.numero_linha = numero_linha
        self.valor_pago = valor_pago
        self.data_processamento = data_processamento
        self.status = status
        self.cod_titulo = cod_titulo
