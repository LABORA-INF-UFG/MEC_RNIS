#Importando as bibliotecas
from flask_restful import Resource, reqparse, request
from v2.receive.exchange import Exchange


#from requests import request
import pika
import json
import connexion


class subscription_post(Resource):

    def post (self, exchange_name, queue_name, severity):
        # Inscrever em um tópico
        #Como posso fazer para me inscrever em um tópico
        Exchange.receive2(exchange_name, queue_name, severity)
        #Exchange.receive3('rab','rab_info', 'rab1')

        return {'message':"sucesso"}, 200

class subscription_delete(Resource):

    def get (self):
        # Ver quais tópicos estou inscrito
        return {'message':"sucesso"}, 200

    def put (self):
        # Modificar a assinatura de tópicos
        return {'message':"sucesso"}, 200
    
    def delete (self):
        # Cancelar/deletar a assinatura de um tópicos
        return {'message':"sucesso"}, 200
