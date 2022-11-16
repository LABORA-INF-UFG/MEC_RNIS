#Importando as bibliotecas
from flask_restful import Resource, reqparse, request
from v2.models.rab_info import RabInfoModel
from v2.receive.exchange import Exchange
from v2.exemplo_dados.rab_info import rabinfos2

#from requests import request
import pika
import json
import connexion

 
class RabInfo(Resource):

    # Teste com o RabbitMQ
    def get (self):

        Exchange.receive('rab','rab_info')
        return {'message':"sucesso"}, 200

class RabInfo2(Resource):

    # Post enviando informações para um RabbitMQ.
    def post(self, app_instance_id):

        # Pega os dados enviados via post.
        dados = request.get_json()
        
        # Criando um objeto do tipo rab_info
        rab_objeto = RabInfoModel(app_instance_id, **dados)
        
        # Como enviar um json 
        rab_JSON = rab_objeto.json()
	
	    # Manda o json para a Exchange que envia para o RabbitMQ
        Exchange.emit('rab','rab_info',rab_JSON)

        '''
        #Serializa o objeto
        dados_1 = json.dumps(rab_JSON)
        #Deserializa o objeto
        dados_2 = json.loads(dados_1)
        '''
        #return {'message':"sucesso"}, 200
        return rab_JSON, 200
