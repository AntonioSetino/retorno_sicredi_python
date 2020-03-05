from flask_restful import Api
from flask import Flask
from controllers import RetornoController
from controllers import TituloController

app = Flask(__name__)
api = Api(app)

api.add_resource(RetornoController, '/sicredi/retorno/<nome_arquivo>')
api.add_resource(TituloController, '/sicredi/titulo/<numero_documento>')


if __name__ == '__main__':
    app.run()

# pip install python-string-utils (string utils)
# pip install flask flask-jsonpify flask-restful (pra criar API)
