import pika, requests
import sqlite3

# Configuração do banco de dados
DB_NAME = 'applications.db'


# Função para obter todos os clientes com o mesmo tópico
def listar_callback_apps_por_notification2(NotificationSubscription):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT callback_uri FROM applications WHERE NotificationSubscription = ?', (NotificationSubscription,))
    resultados = cursor.fetchall()
    conn.close()
    
    return resultados

 # Conectando com o RabbitMQ
credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
connection = pika.BlockingConnection(parameters) # Connection (parameters)
        # Conectando com o RabbitMQ
channel = connection.channel() # CRia o CHannel com a connection

        # Declaração do exchange e da fila
channel.exchange_declare(exchange="plmn", exchange_type='topic')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
  #print ("Entrou no setup_rabbitmq")
        # Binding da fila ao tópico desejado



routing_key = 'my_topic'
channel.queue_bind(exchange="plmn", queue=queue_name, routing_key=routing_key)



# Função que será executada quando uma mensagem for recebida
def callback(ch, method, properties, body):
    print(f"Recebido '{body.decode()}'")



# Define o callback para processar mensagens recebidas
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Inicia a escuta por mensagens
channel.start_consuming()