from string_utils import is_full_string
from subocorrencias import Subocorrencias


class Registro(object):

    def __init__(self, linha, numero_documento, ocorrencia, data_pagamento, valor_pago, tarifa, subocorrencias):
        self.titulo = None
        self.linha = linha
        self.numero_documento = numero_documento
        self.ocorrencia = ocorrencia
        self.data_pagamento = data_pagamento
        self.valor_pago = valor_pago
        self.tarifa = tarifa
        self.subocorrencias = Subocorrencias.retornar(self.ocorrencia, subocorrencias)

        if (not is_full_string(self.data_pagamento) or not is_full_string(self.valor_pago)
            or not is_full_string(self.numero_documento) or not is_full_string(self.ocorrencia)):
            self.inconsistente = True
        else:
            self.inconsistente = False

    def to_dict(self):
        return self.__dict__
