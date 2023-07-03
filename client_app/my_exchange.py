## Esse script se inscreve no topico rab consome informações e faz um calculo

import pika
import json

def callback(ch, method, properties, body):
    # Conversão do corpo da mensagem para um valor numérico


    # Acesso aos dados desserializados
    #print(data["app_instance_id"])  # Saída: John

    try:
        data = json.loads(body)
    except ValueError:
        print("o body é :", data['cell_user_info']['ue_info']['erab_info']['erab_id'])
        print("Erro: Valor inválido recebido")
        return
    value = data['cell_user_info']['ue_info']['erab_info']['erab_id']
    # Realiza a soma do valor recebido
    global total
    total += value

    # Exibe o valor atual do total
    print("Valor recebido:", value)
    print("Total:", total)

def callback2(ch, method, properties, body):
    # Conversão do corpo da mensagem para um valor numérico


    # Acesso aos dados desserializados
    #print(data["app_instance_id"])  # Saída: John

    try:
        data = json.loads(body)
    except ValueError:
        print("o body é :", data['cell_user_info']['ue_info']['erab_info']['erab_id'])
        print("Erro: Valor inválido recebido")
        return
    valor_input = data['cell_user_info']['ue_info']['erab_info']['erab_id']
    # Realiza a soma do valor recebido


    # Chama a função calcular passando o valor de entrada e obtém o resultado
    resultado_calculo = calcular(valor_input)


def consume_rab():
    credentials = pika.PlainCredentials(username='admin', password='123456')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='rab', exchange_type='fanout', durable=True)
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    #Já criamos uma troca de fanout e uma queue. Agora precisamos dizer à exchange para enviar mensagens para nossa queue. Essa relação entre a exchange e uma queue é chamada de ligação .
    channel.queue_bind(exchange='rab', queue=queue_name)
    
     # Configuração do consumidor
    channel.basic_consume(queue=queue_name, on_message_callback=callback2, auto_ack=True)
    
    # Inicia a escuta por mensagens
    print('Aguardando mensagens...')
    channel.start_consuming()

def calcular(valor):
    resultado = valor * 2  # Exemplo de cálculo: multiplicação por 2
        
    # Exibe o resultado do cálculo
    print("O resultado do cálculo é:", resultado)
    return resultado



total = 0  # Variável global para armazenar o total da soma

consume_rab()
