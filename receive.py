import threading
import pika
import requests, time
from flask import Flask
import subprocess
from bd.table import listar_callback_apps_por_notification2


numero = "10"
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
        #output_file = open('mensagens_plmn.txt', 'w')
        
        # Função que será executada quando uma mensagem for recebida
        def callback(ch, method, properties, body):
            message_with_time = body.decode()
            start_time_str, message = message_with_time.split(':', 1)
            start_time = float(start_time_str)
            
            # Calcule o tempo de entrega
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Tempo total de entrega: {elapsed_time} segundos") 
            data = {'message': message}
            
            try:
                
                resultados = listar_callback_apps_por_notification2("plmn")
                # Use uma compreensão de lista para extrair os links
                links = [item[0] for item in resultados]
                # Loop for para imprimir todas as URLs
                for callback_url_1 in links:
                    response = requests.post(callback_url_1, json=message_with_time)
                    #response = requests.post(callback_url_1, json=data)
                    caminho_arquivo = "/l/disk0/mcunha/Documentos/ufg/MEC_RNIS/locust/05_minutos_client_800users_1s_2_mec_apps/tempos_decorridos_plmn_"+numero+".txt"

                    with open(caminho_arquivo, "a") as arquivo:
                        arquivo.write(f"{elapsed_time}\n")
                    #output_file.write(message + '\n')
                    
                    response.raise_for_status()
                    #print(f"Callback (PLMN) enviado com sucesso para {callback_url_1}")
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
        #output_file = open('mensagens_rab.txt', 'w')

        # Função que será executada quando uma mensagem for recebida
        def callback(ch, method, properties, body):
             
            message_with_time = body.decode()
            start_time_str, message = message_with_time.split(':', 1)
            start_time = float(start_time_str)
            
            # Calcule o tempo de entrega
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Tempo total de entrega: {elapsed_time} segundos")
            
            data = {'message': message}

            try:

                # Use uma compreensão de lista para extrair os links
                resultados = listar_callback_apps_por_notification2("rab")
                links = [item[0] for item in resultados]
                # Loop for para imprimir todas as URLs
                for callback_url_1 in links:
                    response = requests.post(callback_url_1, json=message_with_time)
                    #response = requests.post(callback_url_1, json=data)
                     # Salve o tempo decorrido em um arquivo de texto
                        # Especifique o caminho completo para o arquivo "tempos.txt"
                    caminho_arquivo = "/l/disk0/mcunha/Documentos/ufg/MEC_RNIS/locust/05_minutos_client_800users_1s_2_mec_apps/tempos_decorridos_rab_"+numero+".txt"

                    with open(caminho_arquivo, "a") as arquivo:
                        arquivo.write(f"{elapsed_time}\n")
                    #output_file.write(message + '\n')
                    
                    response.raise_for_status()
                    #print(f"Callback (RAB) enviado com sucesso para {callback_url_1}")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar o callback (RAB): {e}")

        # Define o callback para processar mensagens recebidas
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Inicia a escuta por mensagens
        channel.start_consuming()
    except Exception as e:
        print(f"Erro ao receber mensagens (RAB): {str(e)}")
    
# Função para executar uma API em uma thread
def run_api(api_file, port):
    subprocess.call(['python3', api_file, '--port', str(port)])
   

if __name__ == '__main__':
    api1_file = 'api_1.py'
    port_api1 = 5000

    # Crie threads para executar cada API
    thread1 = threading.Thread(target=run_api, args=(api1_file, port_api1))

    thread_plmn = threading.Thread(target=receive_and_send_messages_plmn)
    thread_rab = threading.Thread(target=receive_and_send_messages_rab)

    # Inicie as threads
    thread1.start()
    time.sleep(10)
    
    # Iniciar as threads
    thread_plmn.start()
    thread_rab.start()
    print("receive ok")
    #app.run(port=8085)

    # Aguarde até que ambas as threads terminem
    thread1.join()