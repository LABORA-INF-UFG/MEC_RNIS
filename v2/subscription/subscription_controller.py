#Importando as bibliotecas
import json
from flask_restful import Resource, reqparse, request
from v2.receive.exchange import Exchange
from flask import Flask, request, jsonify, Response

""" def subscription_post(notificationsubscription):

    if notificationsubscription == "CellChangeSubscription":

        print("CellChangeSubscription.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')
        
        # return resposta


    elif notificationsubscription == "RabEstSubscription":

        print ("notificationsubscription")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        # return resposta


    elif notificationsubscription == "RabModSubscription":

        print ("notificationsubscription")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        # return resposta


    elif notificationsubscription == "RabRelSubscription":

        print("RAB Release.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        # return resposta


    elif notificationsubscription == "MeasRepUeSubscription":

        print("UE Measurement Report.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        # return resposta

    elif notificationsubscription == "MeasTaSubscription":

        print("UE Timing Advance.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        # return resposta


    elif notificationsubscription == "CaReconfSubscription":

        print("Carrier Aggregation Reconfig.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        # return resposta

    elif notificationsubscription == "S1BearerSubscription":

        print("S1 Bearer Notification.")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        #return resposta

    elif notificationsubscription == "NrMeasRepUeSubscription":

        print("5G UE Measurement Report .")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        #return resposta
    
    elif notificationsubscription == "SubscriptionLinkList":

        print("Teste SubscriptionLinkList")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        #return resposta
    
    elif notificationsubscription == "plmn":

        print("Teste plmn")

        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')

        return resposta

    elif notificationsubscription == "rab":
        #callback_uri= "asdf"
        print("Teste rab")

        #resposta = Response(Exchange.generate_data1(notificationsubscription)(), mimetype='text/plain')
        resposta = Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')
        #Response(Exchange.generate_data(notificationsubscription)(), mimetype='text/plain')
        print ("Passando no subscription_controller")

        #return "ok"
        return resposta

    else:

        print("Não foi possível determinar o valor.")
        
        return {'message':"Chegou no ultimo passo"}, 401
    
 """
def subscription_verification(notificationsubscription):

    if notificationsubscription == "CellChangeSubscription":

        return "ok"


    elif notificationsubscription == "RabEstSubscription":

        return "ok"


    elif notificationsubscription == "RabModSubscription":

        return "ok"


    elif notificationsubscription == "RabRelSubscription":

        return "ok"


    elif notificationsubscription == "MeasRepUeSubscription":

        return "ok"

    elif notificationsubscription == "MeasTaSubscription":

        return "ok"


    elif notificationsubscription == "CaReconfSubscription":

        return "ok"

    elif notificationsubscription == "S1BearerSubscription":

        return "ok"

    elif notificationsubscription == "NrMeasRepUeSubscription":

        return "ok"
    
    elif notificationsubscription == "SubscriptionLinkList":

        return "ok"
    
    elif notificationsubscription == "plmn":

        return "ok"

    elif notificationsubscription == "rab":

        return "ok"

    else:

        return "nok"


def Notification_CellChangeSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("CellChangeSubscription")(), mimetype='text/plain')
    return resposta

def Notification_RabEstSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("RabEstSubscription")(), mimetype='text/plain')
    return resposta

def Notification_RabModSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("RabModSubscription")(), mimetype='text/plain')
    return resposta

def Notification_RabRelSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("RabRelSubscription")(), mimetype='text/plain')
    return resposta

def Notification_MeasRepUeSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("MeasRepUeSubscription")(), mimetype='text/plain')
    return resposta

def Notification_MeasTaSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("MeasTaSubscription")(), mimetype='text/plain')
    return resposta

def Notification_CaReconfSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("CaReconfSubscription")(), mimetype='text/plain')
    return resposta

def Notification_S1BearerSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("S1BearerSubscription")(), mimetype='text/plain')
    return resposta

def Notification_NrMeasRepUeSubscription():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("NrMeasRepUeSubscription")(), mimetype='text/plain')
    return resposta

def Notification_SubscriptionLinkList():

    #Chama a função subscription_post
    #result = subscription_post("rab") # Chama o subscription_post
    resposta = Response(Exchange.generate_data("SubscriptionLinkList")(), mimetype='text/plain')
    return resposta

def Notification_rab():
    try:
        print ("Notification Rab")
        #Chama a função subscription_post
        Response(Exchange.init_rab("rab"))
        #resposta = Response(Exchange.generate_data_rab("rab")(), mimetype='text/plain')
        resposta = Response(Exchange.receive_messages_rab())
        return resposta
    except Exception as e:
        # Capture a exceção e imprima-a (ou registre-a em um arquivo de log)
        print(f"Exceção em Notification_rab: {e}")

def Notification_plmn():
    try:
        print ("Notification Plmn")
        #Chama a função subscription_post
        Response(Exchange.init_plmn("plmn"))
        #resposta = Response(Exchange.generate_data_plmn("plmn")(), mimetype='text/plain')
        resposta = Response(Exchange.receive_messages_plmn())
        return resposta
    except Exception as e:
        # Capture a exceção e imprima-a (ou registre-a em um arquivo de log)
        print(f"Exceção em Notification_plmn: {e}")
        

def Notifications():

    Notification_rab()
    #print ("entrou no notifications e passou do rab")
    Notification_plmn()
    
    #Notification_CellChangeSubscription()
    #Notification_RabEstSubscription()
    #Notification_RabModSubscription()
    #Notification_RabRelSubscription()
    #Notification_MeasRepUeSubscription()
    #Notification_MeasTaSubscription()
    #Notification_CaReconfSubscription()
    #Notification_S1BearerSubscription()
    #Notification_NrMeasRepUeSubscription()
    #Notification_SubscriptionLinkList()



    return "ok"