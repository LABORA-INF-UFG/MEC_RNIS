""" import pika

# Variável global para manter a referência do canal
channel = None

def start_consumer():
    global channel

    # Configuração da conexão RabbitMQ
    # Conectando com o RabbitMQ
    credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
    parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
    connection = pika.BlockingConnection(parameters) # Connection (parameters)
    # Conectando com o RabbitMQ
    channel = connection.channel() # CRia o CHannel com a connection
    severity = "r" # Cria o servirity com o mesmo nome da exchange
    
    # Declaração do exchange e da fila
    channel.exchange_declare(exchange='r', exchange_type='topic')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Binding da fila ao tópico desejado
    routing_key = 'my_topic'
    channel.queue_bind(exchange='r', queue=queue_name, routing_key=routing_key)

    # Função de callback que será chamada quando uma mensagem for recebida
    def callback(ch, method, properties, body):
        # Processar os dados da mensagem
        data = body.decode('utf-8')
        print('Mensagem recebida:', data)

        # Confirmar o processamento da mensagem
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Consumir as mensagens do tópico
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    # Iniciar o consumo das mensagens
    print('Iniciando o consumidor RabbitMQ...')
    channel.start_consuming()

def stop_consumer():
    global channel

    if channel is not None and channel.is_open:
        # Parar o consumo de mensagens
        channel.stop_consuming()

        # Fechar a conexão e o canal
        channel.close()

        print('Consumidor RabbitMQ fechado.')
    else:
        print('Nenhum consumidor RabbitMQ em execução.')

# Obter o comando do usuário (start ou stop)
command = input('Digite o comando (start/stop): ')

if command == 'start':
    start_consumer()
elif command == 'stop':
    stop_consumer()
else:
    print('Comando inválido. Use "start" para iniciar ou "stop" para fechar o consumidor RabbitMQ.')
 """


import pika
import threading

def start_consumer():
    # Configuração da conexão RabbitMQ
        # Conectando com o RabbitMQ
    credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
    parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
    connection = pika.BlockingConnection(parameters) # Connection (parameters)
    # Conectando com o RabbitMQ
    channel = connection.channel() # CRia o CHannel com a connection

    # Declaração do exchange e da fila
    channel.exchange_declare(exchange='my_exchange', exchange_type='topic')
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Binding da fila ao tópico desejado
    routing_key = 'my_topic'
    channel.queue_bind(exchange='my_exchange', queue=queue_name, routing_key=routing_key)

    # Função de callback que será chamada quando uma mensagem for recebida
    def callback(ch, method, properties, body):
        # Processar os dados da mensagem
        data = body.decode('utf-8')
        print('Mensagem recebida:', data)

        # Confirmar o processamento da mensagem
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Definir o callback de retorno de chamada
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print('Consumidor RabbitMQ iniciado. Pressione "stop" para parar o consumidor.')

    # Aguardar o comando "stop" para parar o consumidor
    while True:
        command = input()

        if command == 'stop':
            # Parar o consumo de mensagens
            channel.stop_consuming()

            # Fechar a conexão e o canal
            channel.close()

            print('Consumidor RabbitMQ fechado.')
            break

    # Fechar a conexão ao sair do loop
    connection.close()

# Iniciar o consumidor RabbitMQ
start_consumer()
