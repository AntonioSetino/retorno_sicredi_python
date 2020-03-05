import psycopg2
from datetime import datetime


class Conexao(object):

    def __init__(self):
        self.__ip = '192.168.1.150'
        self.__porta = '5432'
        self.__usuario = 'pegasus'
        self.__senha = 'pegasus2017'
        self.__banco = 'dev_erp_pegasus_materializacao'

    def __conectar(self):
        return psycopg2.connect(host=self.__ip, port=self.__porta, user=self.__usuario, password=self.__senha, database=self.__banco)

    # retorna mais de um registro
    def listar(self, query):
        conexao = self.__conectar()
        cur = conexao.cursor()
        cur.execute(query)
        registros = cur.fetchall()
        cur.close()
        conexao.close()
        return registros

    # retorna um unico registro
    def consultar(self, query):
        conexao = self.__conectar()
        cur = conexao.cursor()
        cur.execute(query)
        registro = cur.fetchone()
        cur.close()
        conexao.close()
        return registro

    def executar(self, query):
        conexao = self.__conectar()
        cur = conexao.cursor()
        cur.execute(query)
        conexao.commit()
        cur.close()
        conexao.close()
