#!/usr/bin/env python
import pika, json, requests, time
from bd.table import listar_callback_apps_por_notification2, get_application_list
import concurrent.futures

global continue_running

global request_count


# Variável global para verificar se a API deve continuar retornando informações
continue_running = True
request_count = 0
class Exchange():

    # Função para configurar a conexão RabbitMQ
    def setup_rabsbitmq(NotificationSubscription):
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

                return channel, queue_name, connection
            except pika.exceptions.AMQPConnectionError:
                print("Falha na conexão com RabbitMQ. Tentando novamente em 5 segundos...")
                time.sleep(5)
                break

    # publica as informações
    def emit_rab(dados, notif):
        
        channel, queue_name, connection = Exchange.setup_rabsbitmq(notif)
        
        """ 
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
        """


        # serializando os dados com o json.dumps
        mensagem = json.dumps(dados)

        # Registre o tempo de início do envio
        start_time = time.time()
        # Envie o tempo de início junto com a mensagem
        message_with_time = f"{start_time}:{mensagem}"

        # Publicação da mensagem
        channel.basic_publish(exchange=notif, routing_key='my_topic', body=message_with_time)
        print('Mensagem publicada no tópico RabbitMQ', notif )

        # Fechar a conexão
        connection.close()

        return mensagem

    # publica as informações
    def emit_plmn(dados, notif):

        channel, queue_name, connection = Exchange.setup_rabsbitmq(notif)
        
        
        """ # Conectando com o RabbitMQ
        credentials = pika.PlainCredentials(username='admin', password='123456') # Credentials (user e password)
        parameters = pika.ConnectionParameters(host='localhost',credentials=credentials) # Parameters (host e credentials)
        connection = pika.BlockingConnection(parameters) # Connection (parameters)
        # Conectando com o RabbitMQ
        channel = connection.channel() # Cria o CHannel com a connection
        
        # Declaração do exchange
        channel.exchange_declare(exchange=notif, exchange_type='topic')

        # Dados para publicação
        routing_key = 'my_topic'
        """
        # serializando os dados com o json.dumps
        mensagem = json.dumps(dados)

        # Registre o tempo de início do envio
        start_time = time.time()
        # Envie o tempo de início junto com a mensagem
        message_with_time = f"{start_time}:{mensagem}"

        # Publicação da mensagem
        channel.basic_publish(exchange=notif, routing_key='my_topic', body=message_with_time)
        print('Mensagem publicada no tópico RabbitMQ', notif)

        # Fechar a conexão
        connection.close()

        return mensagem


    def emit(dados, notif):
        print ("notif", notif)
        #max_threads = 20  # Ajuste conforme necessário
        if notif == "rab":
            # Configuração do ThreadPoolExecutor com um número máximo de threads

            with concurrent.futures.ThreadPoolExecutor() as executor:
                # Mapeie a função para os argumentos em paralelo
                print("Entrou no rab")
                executor.map(Exchange.emit_rab(dados, notif))
        else: 
            if notif == "plmn":
                # Configuração do ThreadPoolExecutor com um número máximo de threads
               
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    # Mapeie a função para os argumentos em paralelo
                    print("Entrou no plmn")
                    executor.map(Exchange.emit_plmn(dados, notif))

###############################################################################

""" 
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
 """