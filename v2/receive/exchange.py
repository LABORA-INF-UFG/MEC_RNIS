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
    def receive(exchange_name, queue_name, severity):
        # Conectando com o RabbitMQ
        connection = Exchange.connect()
        channel = connection.channel()

        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)
        
        #result = channel.queue_declare(queue=queue_name, durable=True)
        #queue_name_new = result.method.queue
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=severity)

        def callback(ch, method, properties, body):
            # Neste momento estamos pegando o body e deserializando com o json.loads
            body = json.loads(body)
            print("CHEGUEI")
             # Retorna os dados em formato JSON
            print (body)
            #return(body)
                ##
                # https://acervolima.com/ler-e-escrever-em-arquivos-de-texto-em-python/
                #
                # Somente gravação ('w'): Abra o arquivo para gravação. Para o arquivo existente, os dados 
                #    são truncados e sobrescritos. A alça é posicionada no início do arquivo. Cria o arquivo
                #    se ele não existir.
                #
                # Append Only ('a') : Abra o arquivo para gravação. O arquivo é criado se não existir. 
                #    A alça é posicionada no final do arquivo. Os dados que estão sendo gravados serão 
                #    inseridos ao final, após os dados existentes
                #
                ##

            # Aqui estamos salvando esta informação em um arquivo .json
            #with open('/home/kaique/Documentos/Teste_API_RNIS_1.9/v2/receive/file.json', 'a') as f:
            #    json.dump(body, f, sort_keys=True)    
          
            
        # auto_ack=True Faz com que as mensagens sejam apagadas da queue
        channel.basic_consume(queue=queue_name, on_message_callback=callback,  auto_ack=True)

        channel.start_consuming()

        # Tenho que fechar a conexão, A questão e como fechar ela corretamente.

    # Recebe mensagens
    def receive2(exchange_name, queue_name, severity):
        # Conectando com o RabbitMQ
        connection = Exchange.connect()
        channel = connection.channel()

        # declara a queue
        #channel.queue_declare(queue=queue_name, durable=True)
        
        channel.exchange_declare(exchange=exchange_name, exchange_type='fanout', durable=True)

        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=severity)

        print(' [*] Waiting for logs. To exit press CTRL+C')

        def callback(ch, method, properties, body):
            print(" [x] %r" % body)

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        channel.start_consuming()




    
    def receive3(exchange_name, queue_name, severity):
        # Conectando com o RabbitMQ
        connection = Exchange.connect()
        channel = connection.channel()

        # declara a queue
        #channel.queue_declare(queue=queue_name, durable=True)
        
        channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

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
    def emit3(exchange_name, queue_name, severity, dados):
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
        
        channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)
        
        channel.basic_publish(exchange=exchange_name, routing_key=queue_name, body=mensagem)

        # Antes de sair do programa, precisamos ter certeza de que os buffers de rede foram liberados e 
        # nossa mensagem foi realmente entregue ao RabbitMQ. Podemos fazê-lo fechando suavemente a conexão.
        connection.close()
    