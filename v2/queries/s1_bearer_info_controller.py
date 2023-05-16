#Importando as bibliotecas
from flask_restful import Resource, reqparse, request
from v2.models.s1_bearer_info import S1BearerInfoModel
from v2.receive.exchange import Exchange

#from requests import request
import pika
import json
import connexion

 
#class S1BearerInfo(Resource):

    # Teste com o RabbitMQ
#    def get (self):

#        Exchange.receive2('s1bearer','s1bearer_info', 's1bearer_1')
#        return {'message':"sucesso"}, 200


class S1BearerInfo2(Resource):

    # Post enviando informações para um RabbitMQ.
    def post(self):

        # Pega os dados enviados via post.
        dados = request.get_json()
        
        # Criando um objeto do tipo rab_info
        s1bearer_objeto = S1BearerInfoModel(**dados)
        
        # Como enviar um json 
        s1bearer_JSON = s1bearer_objeto.json()
	
	    # Manda o json para a Exchange que envia para o RabbitMQ
        Exchange.emit('s1bearer','s1bearer_info','s1bearer_1', s1bearer_JSON)

        #return {'message':"sucesso"}, 200
        return s1bearer_JSON, 200
