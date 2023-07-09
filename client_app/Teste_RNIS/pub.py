## Este script publica no my_exchange do rabbitmq

import pika

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

# Publicação da mensagem
channel.basic_publish(exchange='rab', routing_key=routing_key, body=message)

print('Mensagem publicada no tópico RabbitMQ.')

# Fechar a conexão
connection.close()