from flask import Flask
import pika
import requests

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
        output_file = open('mensagens.txt', 'w')
        # Função que será executada quando uma mensagem for recebida
        def callback(ch, method, properties, body):
            message = body.decode()
            print(f"Recebido '{message}'")

            # Enviar a mensagem via callback para http://localhost:8002/callback5
            callback_url = 'http://localhost:8009/callback3'
            data = {'message': message}
            # Arquivo para salvar as mensagens

            try:
                response = requests.post(callback_url, json=data)
                output_file.write(message + '\n')
                response.raise_for_status()
                print(f"Callback enviado com sucesso para {callback_url}")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar o callback: {e}")

        # Define o callback para processar mensagens recebidas
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Inicia a escuta por mensagens
        channel.start_consuming()
    except Exception as e:
        print(f"Erro ao receber mensagens: {str(e)}")


@app.route('/api/receive', methods=['GET'])
def start_receiving():
    try:
        receive_and_send_messages_plmn()
        return "Recebendo mensagens do RabbitMQ e enviando via callback."
    except Exception as e:
        return f"Erro: {str(e)}", 500

if __name__ == '__main__':
    receive_and_send_messages_plmn()  # Inicia o processo de recebimento e envio via callback automaticamente
    app.run(debug=True, port=8085)  # Use a porta 8080 em vez da 5000