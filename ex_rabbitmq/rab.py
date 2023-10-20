import pika

# Conectando com o RabbitMQ
credentials = pika.PlainCredentials(username='admin', password='123456')
parameters = pika.ConnectionParameters(host='localhost', credentials=credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare(exchange="rab", exchange_type='topic')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

routing_key = 'my_topic'
channel.queue_bind(exchange="rab", queue=queue_name, routing_key=routing_key)

# Arquivo para salvar as mensagens
output_file = open('mensagens.txt', 'w')

# Função que será executada quando uma mensagem for recebida
def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Recebido '{message}'")
    
    # Escreve a mensagem no arquivo
    output_file.write(message + '\n')

# Define o callback para processar mensagens recebidas
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Inicia a escuta por mensagens
channel.start_consuming()