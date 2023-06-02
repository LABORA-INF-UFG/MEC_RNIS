#!/usr/bin/env python
from multiprocessing import connection
from sqlite3 import connect
import pika 
import time
import json
import sys
from flask import jsonify

class Exchange():

    # Conectando com o RabbitMQ
    def connect():
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456')
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials)
        connection = pika.BlockingConnection(parameters)

        return connection

    # Recebe mensagens
    def receiver(exchange_name, queue_name, severity):
        # Conectando com o RabbitMQ
        connection = Exchange.connect()
        channel = connection.channel()

        # declara a queue
        #channel.queue_declare(queue=queue_name, durable=True)
        
        # declara a exchange
        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=severity)

        print(' [*] Waiting for logs. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            print(" [x] %r" % body)

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        channel.start_consuming()

      # Envia mensagens
    def emit(exchange_name, queue_name, severity, dados):
        # Conectando com o RabbitMQ
        connection = Exchange.connect()
        channel = connection.channel()
        #
        # 
        # Pego os dados e serializo aqui!
        # 
        # #

        # serializando os dados com o json.dumps
        mensagem = json.dumps(dados)

        # declara a queue
        channel.queue_declare(queue=queue_name, durable=True)
        
        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)
        
        channel.basic_publish(exchange=exchange_name, routing_key=queue_name, body=mensagem)

        # Antes de sair do programa, precisamos ter certeza de que os buffers de rede foram liberados e 
        # nossa mensagem foi realmente entregue ao RabbitMQ. Podemos fazê-lo fechando suavemente a conexão.
        connection.close()

        # Envia mensagens