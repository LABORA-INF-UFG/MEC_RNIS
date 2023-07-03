#Importando as bibliotecas
import json
from flask_restful import Resource, reqparse, request
from v2.receive.exchange import Exchange
from v2.receive.exchange_ex import ExchangeEx
from flask import Flask, request, jsonify

def subscription_post(notificationsubscription):

    if notificationsubscription == "CellChangeSubscription":
        Exchange.receiver3(notificationsubscription)
        print("CellChangeSubscription.")
        return {'message':"sucesso"}, 200

    elif notificationsubscription == "RabEstSubscription":
#       Exchange.receiver(notificationsubscription)
        print ("notificationsubscription", notificationsubscription)
        return {'message':"sucessooooo"}, 200

    elif notificationsubscription == "RabModSubscription":
#       Exchange.receiver(notificationsubscription)
        return {'message':"sucesso"}, 200

    elif notificationsubscription == "RabRelSubscription":
#        Exchange.receiver(notificationsubscription)
        print("RAB Release.")
        return {'message':"sucesso"}, 200

    elif notificationsubscription == "MeasRepUeSubscription":
#       Exchange.receiver(notificationsubscription)
        print("UE Measurement Report.")
        return {'message':"sucesso"}, 200

    elif notificationsubscription == "NrMeasRepUeSubscription":
#       Exchange.receiver(notificationsubscription)
        print("5G UE Measurement Report .")
        return {'message':"sucesso"}, 200

    elif notificationsubscription == "MeasTaSubscription":
#       Exchange.receiver(notificationsubscription)
        print("UE Timing Advance.")
        return {'message':"sucesso"}, 200

    elif notificationsubscription == "CaReconfSubscription":
#       Exchange.receiver(notificationsubscription)
        print("Carrier Aggregation Reconfig.")
        return {'message':"sucesso"}, 200
        
    elif notificationsubscription == "S1BearerSubscription":
#       Exchange.receiver(notificationsubscription)
        print("S1 Bearer Notification.")
        return {'message':"sucesso"}, 200

    elif notificationsubscription == "rab":
        print("Teste rab")
        #resposta = Exchange.receiver3(notificationsubscription)
        resposta = ExchangeEx.receiver(notificationsubscription)

        #json_data = json.dumps(resposta)
        #return {'message': data}, 200

        #Transformar em json#### como passar uma array_list para json
        return resposta
        
    else:
        print("Não foi possível determinar o valor.")
        return {'message':"Chegou no ultimo passo"}, 401
    