#!/usr/bin/env python
from multiprocessing import connection
from sqlite3 import connect
import pika 
import time
import json
import sys
import requests

class ExchangeEx():

    # Conectando com o RabbitMQ
    def connect():
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)

        return connection # Return
    

    # Recebe mensagens Atualemente esta funcionando e retorna uma das mensagens.. O problema é que só retorna uma mensagem
    def receiver(exchange_name):

        # Conectando com o RabbitMQ
        connection = ExchangeEx.connect() # Connection
        channel = connection.channel() # CRia o CHannel com a connection
        severity = exchange_name # Cria o servirity com o mesmo nome da exchange

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

            messages1.append(data)

            # Confirmar o processamento da mensagem
            ch.basic_ack(delivery_tag=method.delivery_tag)

            #channel.stop_consuming()
            ## tenho uma api que recebe estas informações no MEC_RNIS/RabbitMQ/Parte_4_Routing/test_receiver.py
            #A API ESTA PREPARADA PARA RECEBER AS INFORMAÇÕES CONSTANTES
            # Agora como pepara uma aplicação para receber as informações constantimente
            url = 'http://localhost:5001/api/receive'
            try:
                response = requests.post(url, json=messages1)
                response.raise_for_status()  # Verifica se ocorreu algum erro na requisição

                # Processar a resposta da outra API, se necessário
                # ...
                print('Mensagem encaminhada para a outra aplicação:', messages1)

            except requests.exceptions.RequestException as e:
                print('Erro na requisição:', e)

        channel.basic_consume(queue=queue_name, on_message_callback=callback)

        # Inicia a escuta por mensagens
        print('Aguardando mensagens... receiver ExchangeEx')
        channel.start_consuming()

        # Retornar as mensagens para o cliente
        json_data = json.dumps(messages1)

        # Aqui estou passando a lista inteira, tenho que transformar em json para passar
        return messages1
        

    # Envia mensagens
    def emit(exchange_name, queue_name, severity, dados):
        # Conectando com o RabbitMQ
        connection = ExchangeEx.connect()
        channel = connection.channel()

        """ 
        # 
        # Pego os dados e serializo aqui!
        # 
        """

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
