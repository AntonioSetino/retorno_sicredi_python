from flask_restful import Resource
from services import RetornoService
from services import TituloService
from flask import jsonify


class RetornoController(Resource):

    def get(self, nome_arquivo):
        service = RetornoService()
        return service.processar_arquivo('arquivo/%s' % nome_arquivo)


class TituloController(Resource):

    def get(self, numero_documento):
        titulo = TituloService().consultar_titulo(numero_documento, 2)
        if titulo is not None:
            return jsonify(titulo.to_dict())
        else:
            return {}
