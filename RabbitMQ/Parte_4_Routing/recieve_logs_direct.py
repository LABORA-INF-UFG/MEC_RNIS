#!/usr/bin/env python
# pip3 install pika
import pika 
import sys


credentials = pika.PlainCredentials(username='admin', password='123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# Em primeiro lugar, sempre que nos conectamos ao Rabbit, precisamos de uma fila nova e vazia.
#Para fazer isso, poderíamos criar uma fila com um nome aleatório ou, melhor ainda - deixar o servidor escolher um nome de fila aleatório para nós. 
# Em segundo lugar, uma vez que a conexão do consumidor é fechada, a fila deve ser excluída.
# Há uma flag  exclusive 
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue


severities = sys.argv[1:]


if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)


print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))
    
    

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

