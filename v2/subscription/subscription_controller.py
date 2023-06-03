#Importando as bibliotecas
from flask_restful import Resource, reqparse, request
from v2.receive.exchange import Exchange


#from requests import request
import pika
import json
import connexion
from flask import Flask, request, jsonify
global next_id
class subscription_get(Resource):

    def get (self, subscription_type):

        if subscription_type == "CellChangeSubscription ":
            print("Cell Change.")
        
        elif subscription_type == "RabEstSubscription":
            print("RAB Establishment.")

        elif subscription_type == "RabModSubscription ":
            print("RAB Modification.")

        elif subscription_type == "RabRelSubscription ":
            print("RAB Release.")

        elif subscription_type == "MeasRepUeSubscription":
            print("UE Measurement Report.")

        elif subscription_type == "NrMeasRepUeSubscription ":
            print("5G UE Measurement Report .")

        elif subscription_type == "MeasTaSubscription ":
            print("UE Timing Advance.")

        elif subscription_type == "CaReconfSubscription ":
            print("Carrier Aggregation Reconfig.")

        elif subscription_type == "S1BearerSubscription ":
            print("S1 Bearer Notification.")

        else:
            print("Não foi possível determinar o valor.")
        
        # Pega os dados enviados via post.
        dados = request.get_json()
        # Inscrever em um tópico
        #Como posso fazer para me inscrever em um tópico
        Exchange.receiver(**dados)


        return {'message':"sucesso"}, 200

""" 
        O post deve passar como parametro o NotificationSubscription pag. 59 ETSI 012 V2
        
        O corpo da entidade na requisição contém o tipo de dados da assinatura específica 
        do evento RNI que se deseja criar, onde as opções de tipo de dados estão listadas 
        abaixo e definidas nas cláusulas 6.3.2 a 6.3.9 e na cláusula 6.3.11:
            
            • CellChangeSubscription 

            • RabEstSubscription 
            • RabModSubscription 
            • RabRelSubscription 

            • MeasRepUeSubscription
            • MeasTaSubscription 

            • NrMeasRepUeSubscription 

            • CaReconfSubscription 

            • S1BearerSubscription 
            
"""

""" 
    exchange_name = 
            • CellChangeSubscription 
            • RabEstSubscription 
            • RabModSubscription 
            • RabRelSubscription 
            • MeasRepUeSubscription 
            • NrMeasRepUeSubscription 
            • MeasTaSubscription 
            • CaReconfSubscription 
            • S1BearerSubscription 

 """

class subscription_post(Resource):

    def post (self):

        # Pega os dados enviados via post.
        dados = request.get_json()
        notificationsubscription = dados # pegar somente o valor do NotificationSubscription

        if notificationsubscription == "CellChangeSubscription ":
            Exchange.receiver(notificationsubscription)
            print("Cell Change.")
            ids = []
            next_id = 1
            new_id = next_id
            next_id += 1
            ids.append(new_id)
            return jsonify({'id': new_id})
        
        elif notificationsubscription == "RabEstSubscription":
            Exchange.receiver(notificationsubscription)
            print("RAB Establishment.")

        elif notificationsubscription == "RabModSubscription ":
            Exchange.receiver(notificationsubscription)
            print("RAB Modification.")

        elif notificationsubscription == "RabRelSubscription ":
            Exchange.receiver(notificationsubscription)
            print("RAB Release.")

        elif notificationsubscription == "MeasRepUeSubscription":
            Exchange.receiver(notificationsubscription)
            print("UE Measurement Report.")

        elif notificationsubscription == "NrMeasRepUeSubscription ":
            Exchange.receiver(notificationsubscription)
            print("5G UE Measurement Report .")

        elif notificationsubscription == "MeasTaSubscription ":
            Exchange.receiver(notificationsubscription)
            print("UE Timing Advance.")

        elif notificationsubscription == "CaReconfSubscription ":
            Exchange.receiver(notificationsubscription)
            print("Carrier Aggregation Reconfig.")

        elif notificationsubscription == "S1BearerSubscription ":
            Exchange.receiver(notificationsubscription)
            print("S1 Bearer Notification.")

        else:
            print("Não foi possível determinar o valor.")
            return {'message':"sucesso"}, 400
        

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
