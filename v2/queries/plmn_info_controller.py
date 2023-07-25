#Importando as bibliotecas
from flask_restful import Resource, reqparse, request
#from v2.models.rab_info import RabInfoModel
from v2.models.plmn_info import PlmnInfoModel
from v2.receive.exchange import Exchange
#from v2.exemplo_dados.plmn_info import plmninfos


#from requests import request
import pika
import json
import connexion

""" 
class PlmnInfo(Resource):

    def get (self):
        Exchange.receiver('plmn','plmn_info','plmn_1')
        return {'message':"sucesso"}, 200
     """
class PlmnInfo2(Resource):

    # Post enviando informações para um RabbitMQ.
    def post(self, app_instance_id):

        # Pega os dados enviados via post.
        dados = request.get_json()

        # Criando um objeto do tipo rab_info
        plmn_objeto = PlmnInfoModel(app_instance_id, **dados)

        # Como enviar um json 
        plmn_JSON = plmn_objeto.json()

        # Manda o json para a Exchange que envia para o RabbitMQ
        #Exchange.emit('plmn','plmn_info','plmn_1', plmn_JSON)
        Exchange.emit(plmn_JSON)

        #return {'message':"sucesso"}, 200
        return plmn_JSON, 200