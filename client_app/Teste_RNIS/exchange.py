#!/usr/bin/env python
from multiprocessing import connection
from sqlite3 import connect
import pika 
import time
import json
import sys
from flask import jsonify, Flask

global continue_running
# Variável global para verificar se a API deve continuar retornando informações
continue_running = True

class Exchange():


    # Função para verificar se a execução deve ser interrompida
    def continue_r():
        #print ("Continue:", continue_running)
        return continue_running

    def stop():
        global continue_running
        continue_running = False
        #print ("Continue:", Exchange.continue_r())
        return 'API stopped'

    # Função para configurar a conexão RabbitMQ
    def setup_rabbitmq(NotificationSubscription):

    
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)
        # Conectando com o RabbitMQ
        channel = connection.channel() # CRia o CHannel com a connection

        # Declaração do exchange e da fila
        channel.exchange_declare(exchange=NotificationSubscription, exchange_type='topic')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        # Binding da fila ao tópico desejado
        routing_key = 'my_topic'
        channel.queue_bind(exchange=NotificationSubscription, queue=queue_name, routing_key=routing_key)

        return channel, queue_name



    # Função para gerar os dados do RabbitMQ
    def generate_data(NotificationSubscription):

        channel, queue_name = Exchange.setup_rabbitmq(NotificationSubscription)

        def generate():
            for method, properties, body in channel.consume(queue=queue_name, auto_ack=True):
                message = body.decode('utf-8')
                yield message + '\n'
                #print ("continue_running:", Exchange.continue_r())
                # Verifica se a execução deve ser interrompida
                if not Exchange.continue_r():
                    break

        return generate


    def pub(dados):
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)
        # Conectando com o RabbitMQ
        channel = connection.channel() # Cria o CHannel com a connection

        # Declaração do exchange
        channel.exchange_declare(exchange='rab', exchange_type='topic')

        # Dados para publicação
        routing_key = 'my_topic'
        message = 'Hello, RabbitMQ!'

        # serializando os dados com o json.dumps
        mensagem = json.dumps(dados)

        # Publicação da mensagem
        channel.basic_publish(exchange='rab', routing_key=routing_key, body=mensagem)

        print('Mensagem publicada no tópico RabbitMQ.')

        # Fechar a conexão
        connection.close()

        return mensagem