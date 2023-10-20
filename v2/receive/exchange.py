#!/usr/bin/env python
import pika, json, requests, time
from bd.table import listar_callback_apps_por_notification2, get_application_list

global continue_running

global request_count


# Variável global para verificar se a API deve continuar retornando informações
continue_running = True
request_count = 0
class Exchange():

    # Função para configurar a conexão RabbitMQ
    def setup_rabbitmq_original(NotificationSubscription):
        
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)
        # Conectando com o RabbitMQ
        channel = connection.channel() # CRia o CHannel com a connection

        # Declaração do exchange e da fila
        channel.exchange_declare(exchange=NotificationSubscription, exchange_type='topic')
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        #print ("Entrou no setup_rabbitmq")
        # Binding da fila ao tópico desejado
        routing_key = 'my_topic'
        channel.queue_bind(exchange=NotificationSubscription, queue=queue_name, routing_key=routing_key)

        return channel, queue_name

    # Função para configurar a conexão RabbitMQ
    def setup_rabbitmq(NotificationSubscription):
        while True:
            try:
                        
                # Conectando com o RabbitMQ
                credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
                parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
                connection = pika.BlockingConnection(parameters) # Connection (parameters)
                # Conectando com o RabbitMQ
                channel = connection.channel() # CRia o CHannel com a connection

                # Declaração do exchange e da fila
                channel.exchange_declare(exchange=NotificationSubscription, exchange_type='topic')
                result = channel.queue_declare(queue='', exclusive=True)
                queue_name = result.method.queue
                #print ("Entrou no setup_rabbitmq")
                # Binding da fila ao tópico desejado
                routing_key = 'my_topic'
                channel.queue_bind(exchange=NotificationSubscription, queue=queue_name, routing_key=routing_key)

                return channel, queue_name
            except pika.exceptions.AMQPConnectionError:
                print("Falha na conexão com RabbitMQ. Tentando novamente em 5 segundos...")
                time.sleep(5)
                break

    # publica as informações
    def emit_rab(dados, notif):
        
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)
        # Conectando com o RabbitMQ
        channel = connection.channel() # Cria o CHannel com a connection
        
        # Declaração do exchange
        channel.exchange_declare(exchange=notif, exchange_type='topic')

        # Dados para publicação
        routing_key = 'my_topic'


        # serializando os dados com o json.dumps
        mensagem = json.dumps(dados)

        # Registre o tempo de início do envio
        start_time = time.time()
        # Envie o tempo de início junto com a mensagem
        message_with_time = f"{start_time}:{mensagem}"

        # Publicação da mensagem
        channel.basic_publish(exchange=notif, routing_key=routing_key, body=message_with_time)
        print('Mensagem publicada no tópico RabbitMQ', notif )

        # Fechar a conexão
        connection.close()

        return mensagem

    # publica as informações
    def emit_plmn(dados, notif):
        
        # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)
        # Conectando com o RabbitMQ
        channel = connection.channel() # Cria o CHannel com a connection
        
        # Declaração do exchange
        channel.exchange_declare(exchange=notif, exchange_type='topic')

        # Dados para publicação
        routing_key = 'my_topic'

        # serializando os dados com o json.dumps
        mensagem = json.dumps(dados)

        # Registre o tempo de início do envio
        start_time = time.time()
        # Envie o tempo de início junto com a mensagem
        message_with_time = f"{start_time}:{mensagem}"


        # Publicação da mensagem
        channel.basic_publish(exchange=notif, routing_key=routing_key, body=message_with_time)
        print('Mensagem publicada no tópico RabbitMQ', notif)

        # Fechar a conexão
        connection.close()

        return mensagem
###############################################################################

    # Função para receber mensagens do RabbitMQ
    def receive_messages_rab():
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
            output_file = open('mensagens_rab_100_6_8.txt', 'w')
            # Função que será executada quando uma mensagem for recebida
            def callback(ch, method, properties, body):
                message = body.decode()
                #print(f"Recebido '{message}'")

                # Enviar a mensagem via callback para http://localhost:8002/callback5
                data = {'message': message}

                # Arquivo para salvar as mensagens
                try:
                    resultados = listar_callback_apps_por_notification2("rab")
                    # Use uma compreensão de lista para extrair os links
                    links = [item[0] for item in resultados]
                    for callback_url in links:
                        response = requests.post(callback_url, json=data)
                    
                    output_file.write(message + '\n')
                    response.raise_for_status()
                    #print(f"Callback enviado com sucesso para {callback_url}")

                    
                    
                except requests.exceptions.RequestException as e:
                    print(f"Erro ao enviar o callback: {e}")

            # Define o callback para processar mensagens recebidas
            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

            # Inicia a escuta por mensagens
            channel.start_consuming()
        except Exception as e:
            print(f"Erro ao receber mensagens: {str(e)}")

        # Função para receber mensagens do RabbitMQ
    
    def receive_messages_plmn():
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
            output_file = open('mensagens_plmn_100_6_8.txt', 'w')
            # Função que será executada quando uma mensagem for recebida
            def callback(ch, method, properties, body):
                message = body.decode()
                #print(f"Recebido '{message}'")

                # Enviar a mensagem via callback para http://localhost:8002/callback5
                data = {'message': message}

                # Arquivo para salvar as mensagens
                try:
                    resultados = listar_callback_apps_por_notification2("plmn")
                    # Use uma compreensão de lista para extrair os links
                    links = [item[0] for item in resultados]
                    for callback_url in links:
                        response = requests.post(callback_url, json=data)
                    
                    output_file.write(message + '\n')
                    response.raise_for_status()
                    #print(f"Callback enviado com sucesso para {callback_url}")

                    
                    
                except requests.exceptions.RequestException as e:
                    print(f"Erro ao enviar o callback: {e}")

            # Define o callback para processar mensagens recebidas
            channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

            # Inicia a escuta por mensagens
            channel.start_consuming()
        except Exception as e:
            print(f"Erro ao receber mensagens: {str(e)}")


    def init(NotificationSubscription):
        channel, queue_name = Exchange.setup_rabbitmq(NotificationSubscription)
        #print ("Entrou no init")

    def init_rab(NotificationSubscription):
        channel, queue_name = Exchange.setup_rabbitmq(NotificationSubscription)
        #print ("Entrou no init")

    def init_plmn(NotificationSubscription):
        channel, queue_name = Exchange.setup_rabbitmq(NotificationSubscription)
        #print ("Entrou no init")


    # Função para gerar os dados do RabbitMQ
    def generate_data(NotificationSubscription):
        #print ("dentro do generate")
        channel, queue_name = Exchange.setup_rabbitmq(NotificationSubscription)

        def generate():
            for method, properties, body in channel.consume(queue=queue_name, auto_ack=True):
                message = body.decode('utf-8')
                
                link = "http://localhost:8002/callback5"

                #requests.post(link, json=message)
                # Função para notificar os clientes com o mesmo tópico via requisição POST
                resultados = listar_callback_apps_por_notification2(NotificationSubscription)
                #print ("resultados: ->", resultados[0])


                #resultado2 = get_application_list()
                #print ("resultado2: ", resultado2)
                # Use uma compreensão de lista para extrair os links
                links = [item[0] for item in resultados]

                for linki in links:
                    #print("link-> ", linki)
                    requests.post(linki, json=message)           
                # Atualizar o arquivo JSON com a contagem de requisições
                
                #yield message + '\n'
                #print ("Quero ver se entrou")
                
                
        return generate
    
    # Função para gerar os dados do RabbitMQ
    def generate_data_rab(NotificationSubscription):
        channel, queue_name = Exchange.setup_rabbitmq(NotificationSubscription)

        def generate():
            try:
                for method, properties, body in channel.consume(queue=queue_name, auto_ack=True):
                    try:
                        message = body.decode('utf-8')
                        
                        #requests.post(link, json=message)
                        # Função para notificar os clientes com o mesmo tópico via requisição POST
                        resultados = listar_callback_apps_por_notification2("rab")

                        # Use uma compreensão de lista para extrair os links
                        links = [item[0] for item in resultados]

                        for linki in links:
                            requests.post(linki, json=message)
                        #requests.post("http://localhost:8002/callback_app_4", json=message)
                        # Obtenha a hora atual
                        hora_atual = time.strftime('%H:%M:%S')
                        # Nome do arquivo de texto
                        nome_arquivo = 'horas_20_minutos_rab_500_500_6_8_segundos_2.txt'
                        # Abra o arquivo para escrita (ou crie um novo)
                        with open(nome_arquivo, 'w') as arquivo:
                            # Escreva a hora atual no arquivo
                            arquivo.write(f'Hora atual: {hora_atual}\n')
                    except Exception as e:
                        # Trate a exceção aqui, por exemplo, imprima o erro
                        print(f"Exceção durante a iteração: {e}")
            except Exception as e:
                # Trate a exceção do loop principal aqui, se necessário
                print(f"Exceção no loop principal: {e}")  
                    
        return generate
        
    # Função para gerar os dados do RabbitMQ
    def generate_data_plmn(NotificationSubscription):
        channel, queue_name = Exchange.setup_rabbitmq(NotificationSubscription)

        def generate():
            try:
                for method, properties, body in channel.consume(queue=queue_name, auto_ack=True):
                    try:
                        message = body.decode('utf-8')
                        
                        # Função para notificar os clientes com o mesmo tópico via requisição POST
                        resultados = listar_callback_apps_por_notification2(NotificationSubscription)

                        # Use uma compreensão de lista para extrair os links
                        links = [item[0] for item in resultados]

                        for linki in links:
                            requests.post(linki, json=message)
        
                        # Obtenha a hora atual
                        hora_atual = time.strftime('%H:%M:%S')
                        # Nome do arquivo de texto
                        nome_arquivo = 'horas_20_minutos_plmn_500_500_6_8_segundos_2.txt'
                        # Abra o arquivo para escrita (ou crie um novo)
                        with open(nome_arquivo, 'w') as arquivo:
                            # Escreva a hora atual no arquivo
                            arquivo.write(f'Hora atual: {hora_atual}\n')
                    except Exception as e:
                        # Trate a exceção aqui, por exemplo, imprima o erro
                        print(f"Exceção durante a iteração: {e}")
            except Exception as e:
                # Trate a exceção do loop principal aqui, se necessário
                print(f"Exceção no loop principal: {e}")

                    
        return generate