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
    def setup_rabbitmq(exchange_name):
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)

        # Conectando com o RabbitMQ
        channel = connection.channel() # CRia o CHannel com a connection

        # declara a exchange
        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=exchange_name, queue=queue_name)

        return channel, queue_name, connection

    # Recebe mensagens Atualemente esta funcionando e retorna uma das mensagens.. O problema é que só retorna uma mensagem
    def receiver3(exchange_name):

        channel, queue_name, connection = Exchange.setup_rabbitmq(exchange_name)
            
        # Lista para armazenar as mensagens recebidas
        messages1 = []

        # Função de callback que será chamada quando uma mensagem for recebida
        def callback(ch, method, properties, body):
            # Processar os dados da mensagem
            data = body.decode('utf-8')

            #print ("data:", data)
            # Adicionar a mensagem à lista
            messages1.append(data)
            #messages1.append(body)

            # Confirmar o processamento da mensagem
            ch.basic_ack(delivery_tag=method.delivery_tag)

            #print (body)
            channel.stop_consuming()

            #Exchange.receiver3(exchange_name)

        channel.basic_consume(queue=queue_name, on_message_callback=callback)

        # Inicia a escuta por mensagens
        print('Aguardando mensagens... receiver3')
        channel.start_consuming()

        #Transformar em json#### como passar uma array_list para json

        # Retornar as mensagens para o cliente
        json_data = json.dumps(messages1)
        # Aqui estou passando a lista inteira, tenho que transformar em json para passar
        return messages1   

    # Envia mensagens
    def emit(exchange_name, queue_name, severity, dados):

        # Conectando com o RabbitMQ
        
        channel, queue_name, connection = Exchange.setup_rabbitmq(exchange_name)
        # serializando os dados com o json.dumps
        mensagem = json.dumps(dados)
        
        channel.basic_publish(exchange=exchange_name, routing_key=queue_name, body=mensagem)

        # Antes de sair do programa, precisamos ter certeza de que os buffers de rede foram liberados e 
        # nossa mensagem foi realmente entregue ao RabbitMQ. Podemos fazê-lo fechando suavemente a conexão.
        connection.close()