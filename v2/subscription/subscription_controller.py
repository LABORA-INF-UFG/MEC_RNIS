#Importando as bibliotecas
import json
from flask_restful import Resource, reqparse, request
from v2.receive.exchange import Exchange
from flask import Flask, request, jsonify, Response

def subscription_post(notificationsubscription):

    if notificationsubscription == "CellChangeSubscription":

        print("CellChangeSubscription.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "RabEstSubscription":

        print ("notificationsubscription", notificationsubscription)

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "RabModSubscription":

        print ("notificationsubscription", notificationsubscription)

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "RabRelSubscription":

        print("RAB Release.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "MeasRepUeSubscription":

        print("UE Measurement Report.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "NrMeasRepUeSubscription":

        print("5G UE Measurement Report .")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "MeasTaSubscription":

        print("UE Timing Advance.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "CaReconfSubscription":

        print("Carrier Aggregation Reconfig.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "S1BearerSubscription":

        print("S1 Bearer Notification.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    elif notificationsubscription == "rab":

        print("Teste rab")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta


    else:

        print("Não foi possível determinar o valor.")
        
        return {'message':"Chegou no ultimo passo"}, 401
    