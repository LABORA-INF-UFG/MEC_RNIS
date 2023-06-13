#Importando as bibliotecas
from flask_restful import Resource, reqparse, request
from v2.receive.exchange import Exchange
from flask import Flask, request, jsonify


import pika, json, connexion, uuid

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
        print("Subscription")
        # Pega os dados enviados via post.
        print("Chegou aqui!!!! Subscription_post")
        return {'message':"sucesso"}, 200


class subscription_post_2(Resource):


    """ 
        Cada uma dos tipos de subscrições já devem estar cadastrados no Brocker, 
        Nesse ponto ao efetuar a requisição do tipo Post passando um NotificationSubscription eu devo
        vincular o appRoot a esse tipo de notificação ou seja inscrever esse appRoot no tópico do 
        NotificationSubscription especificado!
    """
    
    def post (self):
 
        dados = request.get_json()
        notificationsubscription = dados['NotificationSubscription'] # pegar somente o valor do NotificationSubscription
        
        if notificationsubscription == "CellChangeSubscription":
            #Exchange.receiver(notificationsubscription)         
            # Gera o id
            #id = str(uuid.uuid4())
            # Retornar o ID como resposta
            print("CellChangeSubscription.")
            return {'message':"sucesso"}, 200

        
        elif notificationsubscription == "RabEstSubscription":
            #Exchange.receiver(notificationsubscription)
            #next_id += 1
            #ids.append(new_id)
            print("RAB Establishment.")
            print ("notificationsubscription", notificationsubscription)
            #return jsonify({'app_id': new_id})
            return {'message':"sucesso"}, 200
        
        elif notificationsubscription == "RabModSubscription":
#            Exchange.receiver(notificationsubscription)
            # Gera o id
            #id = str(uuid.uuid4())
            # Retornar o ID como resposta
            #return jsonify({'id': id})
            return {'message':"sucesso"}, 200

        elif notificationsubscription == "RabRelSubscription":
#            Exchange.receiver(notificationsubscription)
            print("RAB Release.")
            return {'message':"sucesso"}, 200

        elif notificationsubscription == "MeasRepUeSubscription":
#            Exchange.receiver(notificationsubscription)
            print("UE Measurement Report.")
            return {'message':"sucesso"}, 200
        
        elif notificationsubscription == "NrMeasRepUeSubscription":
#            Exchange.receiver(notificationsubscription)
            print("5G UE Measurement Report .")
            return {'message':"sucesso"}, 200

        elif notificationsubscription == "MeasTaSubscription":
#            Exchange.receiver(notificationsubscription)
            print("UE Timing Advance.")
            return {'message':"sucesso"}, 200
        
        elif notificationsubscription == "CaReconfSubscription":
#            Exchange.receiver(notificationsubscription)
            print("Carrier Aggregation Reconfig.")
            return {'message':"sucesso"}, 200
        
        elif notificationsubscription == "S1BearerSubscription":
#            Exchange.receiver(notificationsubscription)
            print("S1 Bearer Notification.")
            return {'message':"sucesso"}, 200

        else:
            print("Não foi possível determinar o valor.")
            return {'message':"error"}, 400
    
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
