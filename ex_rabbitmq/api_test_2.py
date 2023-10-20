import threading
import pika
import requests
from flask import Flask

app = Flask(__name__)


# Função para receber mensagens do RabbitMQ e enviar via callback
def receive_and_send_messages_plmn():
    try:
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456')
        parameters = pika.ConnectionParameters(host='localhost', credentials=credentials)
        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()

        channel.exchange_declare(exchange="plmn", exchange_type='topic')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        routing_key = 'my_topic'
        channel.queue_bind(exchange="plmn", queue=queue_name, routing_key=routing_key)
        output_file = open('mensagens_plmn.txt', 'w')
        #urls = [
        #    "http://localhost:8009/callback3"
        #]
        
        # Função que será executada quando uma mensagem for recebida
        def callback(ch, method, properties, body):
            message = body.decode()
            print(f"Recebido (PLMN) '{message}'")

            # Enviar a mensagem via callback para http://localhost:8009/callback3
            #callback_url = 'http://localhost:8009/callback3'
            data = {'message': message}
            # Arquivo para salvar as mensagens
            
            try:
                
                resultados = listar_callback_apps_por_notification2("plmn")
                # Use uma compreensão de lista para extrair os links
                links = [item[0] for item in resultados]
                # Loop for para imprimir todas as URLs
                for callback_url_1 in links:
                    response = requests.post(callback_url_1, json=data)
                    output_file.write(message + '\n')
                    response.raise_for_status()
                    print(f"Callback (PLMN) enviado com sucesso para {callback_url_1}")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar o callback (PLMN): {e}")

        # Define o callback para processar mensagens recebidas
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Inicia a escuta por mensagens
        channel.start_consuming()
    except Exception as e:
        print(f"Erro ao receber mensagens (PLMN): {str(e)}")

# Função para receber mensagens do RabbitMQ e enviar via callback
def receive_and_send_messages_rab():
    try:
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
        output_file = open('mensagens_rab.txt', 'w')
        #urls = [
        #    "http://localhost:8002/callback_app_4"
        #]

        # Função que será executada quando uma mensagem for recebida
        def callback(ch, method, properties, body):
            message = body.decode()
            print(f"Recebido (RAB) '{message}'")

            # Enviar a mensagem via callback para http://localhost:8002/callback_app_4
            #callback_url = 'http://localhost:8002/callback_app_4'
            data = {'message': message}
            # Arquivo para salvar as mensagens

            try:

                # Use uma compreensão de lista para extrair os links
                resultados = listar_callback_apps_por_notification2("rab")
                links = [item[0] for item in resultados]
                # Loop for para imprimir todas as URLs
                for callback_url_1 in links:
                    response = requests.post(callback_url_1, json=data)
                    output_file.write(message + '\n')
                    response.raise_for_status()
                    print(f"Callback (RAB) enviado com sucesso para {callback_url_1}")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar o callback (RAB): {e}")

        # Define o callback para processar mensagens recebidas
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Inicia a escuta por mensagens
        channel.start_consuming()
    except Exception as e:
        print(f"Erro ao receber mensagens (RAB): {str(e)}")
    """ 
    @app.route('/api/receive', methods=['GET'])
    def start_receiving():
        try:
            # Iniciar as duas funções em threads separadas
            thread_plmn = threading.Thread(target=receive_and_send_messages_plmn)
            thread_rab = threading.Thread(target=receive_and_send_messages_rab)

            # Iniciar as threads
            thread_plmn.start()
            thread_rab.start()

            return "Recebendo mensagens do RabbitMQ e enviando via callback (PLMN e RAB)."
        except Exception as e:
            return f"Erro: {str(e)}", 500 """

if __name__ == '__main__':
    thread_plmn = threading.Thread(target=receive_and_send_messages_plmn)
    thread_rab = threading.Thread(target=receive_and_send_messages_rab)

        # Iniciar as threads
    thread_plmn.start()
    thread_rab.start()
    app.run(port=8085)