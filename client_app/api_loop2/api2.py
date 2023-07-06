import pika
from flask import Flask, Response

app = Flask(__name__)


# Função para configurar a conexão RabbitMQ
def setup_rabbitmq():
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

    return channel, queue_name



# Variável global para verificar se a API deve continuar retornando informações
continue_running = True

# Função para gerar os dados do RabbitMQ
def generate_data():

    channel, queue_name = setup_rabbitmq()

    def generate():
        for method, properties, body in channel.consume(queue=queue_name, auto_ack=True):
            message = body.decode('utf-8')
            yield message + '\n'

            # Verifica se a execução deve ser interrompida
            if not continue_running:
                break

    return generate


# Rota principal que retorna as informações do RabbitMQ continuamente
@app.route('/continuous-data')
def continuous_data():
    return Response(generate_data()(), mimetype='text/plain')


# Função para verificar se a execução deve ser interrompida
def continue_running():
    return continue_running

# Rota para interromper a execução da API
@app.route('/stop')
def stop():
    global continue_running
    continue_running = False
    return 'API stopped'


if __name__ == '__main__':
    app.run()
