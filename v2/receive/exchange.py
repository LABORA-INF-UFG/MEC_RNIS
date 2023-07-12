#!/usr/bin/env python
from multiprocessing import connection
from sqlite3 import connect
import pika 
import time
import json
import sys
from flask import jsonify, Flask

class Exchange():

    # Variável global para manter a referência do canal
    channel = None

    # Conectando com o RabbitMQ
    def connect():
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)

        return connection # Return
    
    # callback basico
    def callback(ch, method, properties, body):
        print(" [x] %r" % body)
        return body

    #Mensagem para salvar os dados do receiver
    messages = []

    # callback2 teste aprimorando o callback basico
    def callback2(ch, method, properties, body):
            # Processar os dados da mensagem
            #data = body.decode('utf-8')
            message = body.decode('utf-8')

            # Adiciona a mensagem à lista de mensagens
            #Exchange.messages.append(message)

            # Retornar a resposta para o assinante
            response = {
                'message': 'Mensagem recebida com sucesso',
                'message': message
            }

            
            # Enviar a resposta para o assinante
            ch.basic_publish(exchange="", routing_key=properties.reply_to,
                         properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                         body=jsonify(response))
            
            # Confirmar o processamento da mensagem
            ch.basic_ack(delivey_tag=method.delivery_tag)
    
    # Recebe mensagens
    def receiver2(exchange_name):
        # Conectando com o RabbitMQ
        connection = Exchange.connect() # Connection
        channel = connection.channel() # CRia o CHannel com a connection
        severity = exchange_name # Cria o servirity com o mesmo nome da exchange

        # declara a queue
        #channel.queue_declare(queue=queue_name, durable=True)
        
        # declara a exchange
        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        
        channel.queue_bind(exchange=exchange_name, queue=queue_name)

        channel.basic_consume(queue=queue_name, on_message_callback=Exchange.callback2, auto_ack=True)

        # Inicia a escuta por mensagens
        print('Aguardando mensagens...')
        channel.start_consuming()

    # Recebe mensagens Atualemente esta funcionando e retorna uma das mensagens.. O problema é que só retorna uma mensagem
    def receiver3(exchange_name):

        # Conectando com o RabbitMQ
        connection = Exchange.connect() # Connection
        channel = connection.channel() # CRia o CHannel com a connection
        severity = exchange_name # Cria o servirity com o mesmo nome da exchange

        # declara a queue
        #channel.queue_declare(queue=queue_name, durable=True)
            
        # declara a exchange
        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange=exchange_name, queue=queue_name)

        #---------------------------------------------------------------#
            
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
