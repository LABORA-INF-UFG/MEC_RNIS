
#!/usr/bin/env python
# pip3 install pika
import pika 
import time

#A ideia e que tenha um cliente que consuma informações direto do RNIS sem conectar com o RABBITMQ
credentials = pika.PlainCredentials(username='admin', password='123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
channel = connection.channel()

#Existem alguns tipos de exchange disponíveis: direct , topic , headers e fanout . 
#Vamos nos concentrar no último - o fanout. Vamos criar uma troca desse tipo e chamá-la de logs :
channel.exchange_declare(exchange='rab', exchange_type='fanout', durable=True)

# Em primeiro lugar, sempre que nos conectamos ao Rabbit, precisamos de uma fila nova e vazia.
#Para fazer isso, poderíamos criar uma fila com um nome aleatório ou, melhor ainda - deixar o servidor escolher um nome de fila aleatório para nós. 
# Em segundo lugar, uma vez que a conexão do consumidor é fechada, a fila deve ser excluída.
# Há uma flag  exclusive 
result = channel.queue_declare(queue='', exclusive=True)

#Neste ponto, result.method.queue contém um nome de fila aleatório. Por exemplo, pode parecer amq.gen-JzTY20BRgKO-HjmUJj0wLg .
queue_name = result.method.queue
#queue_name = 'teste'

#Já criamos uma troca de fanout e uma queue. Agora precisamos dizer à exchange para enviar mensagens para nossa queue. Essa relação entre a exchange e uma queue é chamada de ligação .
channel.queue_bind(exchange='rab', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
