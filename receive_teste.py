import threading
import pika
import requests, time
from flask import Flask
import subprocess
import sys
from bd.table import listar_callback_apps_por_notification2, listar_callback_apps


numero = "1"

# Função para receber mensagens do RabbitMQ e enviar via callback
def receive_and_send_messages(iteracao, current_directory, notification, callback_url):
    try:
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456')
        parameters = pika.ConnectionParameters(host='localhost', credentials=credentials)
        connection = pika.BlockingConnection(parameters)

        channel = connection.channel()

        channel.exchange_declare(exchange=notification, exchange_type='topic')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue

        routing_key = 'my_topic'
        channel.queue_bind(exchange=notification, queue=queue_name, routing_key=routing_key)
        
        # Função que será executada quando uma mensagem for recebida
        def callback(ch, method, properties, body):
            message_with_time = body.decode()
            start_time_str, message = message_with_time.split(':', 1)
            start_time = float(start_time_str)
            
            # Calcule o tempo de entrega
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Tempo total de entrega: {elapsed_time} segundos") 
            #data = {'message': message}
            
            try:
                
                #resultados = listar_callback_apps_por_notification2(notification)
                # Use uma compreensão de lista para extrair os links
                #links = [item[0] for item in resultados]
                # Loop for para imprimir todas as URLs
                #for callback_url_1 in links:
                response = requests.post(callback_url, json=message_with_time)
                    #response = requests.post(callback_url_1, json=data)
                caminho_arquivo = current_directory + "/locust/5_minutos_client_100users_1s_4_mec_apps/tempos_decorridos_"+notification+"_"+iteracao+".txt"

                with open(caminho_arquivo, "a") as arquivo:
                    arquivo.write(f"{elapsed_time}\n")
                    
                    response.raise_for_status()
                    #print(f"Callback ({notification}) enviado com sucesso para {callback_url_1}")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao enviar o callback ({notification}): {e}")

        # Define o callback para processar mensagens recebidas
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Inicia a escuta por mensagens
        channel.start_consuming()
    except Exception as e:
        print(f"Erro ao receber mensagens ({notification}): {str(e)}")





def verifica_thread(iteracao, current_directory):
    primeira_iteracao = True
    
    while True:
        resultados = listar_callback_apps()
        #print ("Resultados: ", resultados)

        if primeira_iteracao:
            #print("Todos os usuários:", resultados)
            primeira_iteracao = False
            for link in resultados:
                print("link = primeiro: ", link)
                thread = threading.Thread(target=receive_and_send_messages, args=(iteracao, current_directory, link[1], link[0]))
                threads.append(thread)
                thread.start()
        else:
            novos_usuarios = set(resultados) - set(usuarios_anteriores)
            #print("-> Novos usuários:", novos_usuarios)
             
            if novos_usuarios:
                print ("passsou no else")
                for link in novos_usuarios:
                    print("link = segundo: ", link)
                    print("Link[0]", link[0])

                    thread = threading.Thread(target=receive_and_send_messages, args=(iteracao, current_directory, link[1], link[0]))
                    threads.append(thread)
                    thread.start()
                

            # Aguarda todas as threads terminarem
            #for thread in threads:
            #    thread.join()
                    
        usuarios_anteriores = set(resultados)
        
        #usuarios_anteriores.update(links)
        time.sleep(3)  # Aguarda 5 segundos antes de imprimir novamente


# Função para executar uma API em uma thread
def run_api(api_file, port):
    subprocess.call(['python3', api_file, '--port', str(port)])
   

if __name__ == '__main__':
    api1_file = 'api_1.py'
    port_api1 = 5000

    iteracao = "1"

    if len(sys.argv) > 1:
        iteracao = sys.argv[1]

    result = subprocess.run(['pwd'], capture_output=True, text=True)
    current_directory = result.stdout.strip()
    # Crie threads para executar cada API
    thread1 = threading.Thread(target=run_api, args=(api1_file, port_api1))

    # Inicia uma thread para cada usuário na lista
    threads = []
    
    #thread_1 = threading.Thread(target=receive_and_send_messages, args=(iteracao, current_directory, 'plmn'))
    #thread_2 = threading.Thread(target=receive_and_send_messages, args=(iteracao, current_directory, 'rab'))
    thread_1 = threading.Thread(target=verifica_thread, args=(iteracao, current_directory))
    # Inicie as threads
    thread1.start()
    time.sleep(10)
    
    # Iniciar as threads
    thread_1.start()
    #thread_2.start()
    print("receive ok")
    #app.run(port=8085)

    # Aguarde até que ambas as threads terminem
    thread1.join()