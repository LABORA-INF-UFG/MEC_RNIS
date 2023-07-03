#!/usr/bin/env python
# pip3 install pika
import pika 
import sys


credentials = pika.PlainCredentials(username='admin', password='123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()

 
channel.exchange_declare(exchange='direct_logs', exchange_type='fanout', durable=True)


severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

message = ' '.join(sys.argv[2:]) or 'Hello World!'

channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)	

print(" [x] Sent %r:%r" % (severity, message))

# Antes de sair do programa, precisamos ter certeza de que os buffers de rede foram liberados e 
# nossa mensagem foi realmente entregue ao RabbitMQ. Podemos fazê-lo fechando suavemente a conexão.
connection.close()

