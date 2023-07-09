#!/usr/bin/env python
from multiprocessing import connection
from sqlite3 import connect
import pika 
import time
import json
import sys
from flask import jsonify, Flask

class Exchange():


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



    # Variável global para verificar se a API deve continuar retornando informações
    continue_running = True

    # Função para gerar os dados do RabbitMQ
    def generate_data(NotificationSubscription):

        channel, queue_name = Exchange.setup_rabbitmq(NotificationSubscription)

        def generate():
            for method, properties, body in channel.consume(queue=queue_name, auto_ack=True):
                message = body.decode('utf-8')
                yield message + '\n'

                # Verifica se a execução deve ser interrompida
                if not Exchange.continue_running:
                    break

        return generate
