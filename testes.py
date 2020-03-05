from dao import NumeroDAO, LogRetornoBancarioDAO
from model import LogRetornoBancario
from datetime import datetime
import timeit

def testar():
    log_retorno = LogRetornoBancario(codigo=NumeroDAO.gerar_id(2, 'LogRetornoBancario'),
                                     cod_empresa=2, motivo='TESTE', numero_documento=123,
                                     numero_linha=0, valor_pago=1.0, data_processamento=datetime.now(),
                                     status='', cod_titulo=None)
    LogRetornoBancarioDAO.salvar(log_retorno)
    print log_retorno


def testar_id():
    print NumeroDAO.gerar_id(2, 'LogRetornoBancario')


if __name__ == '__main__':
    testar()
