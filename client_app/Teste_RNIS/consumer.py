import requests
import time

def consume():
    url = 'http://127.0.0.1:5000/app_client/rni/v2'  # URL da API
    endpoint = '/subscriptions'  # Endpoint específico da API
    data = {"NotificationSubscription" : "rab"} 

    response = requests.post(url + endpoint, json=data, stream=True)

    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Iterar sobre as informações recebidas
        for data in response.iter_lines():
            if data:
                # Decodificar o JSON recebido
                json_data = data.decode('utf-8')
                #print("Teste")
                print(json_data)  # Exibir as informações na tela
    else:
        print('Erro na requisição:', response.status_code)

def cancel():
    url = 'http://127.0.0.1:5000/app_client/rni/v2'  # URL da API
    endpoint = '/subscriptions'  # Endpoint específico da API
    data = {"id" : "b3e6b48f-3924-4ead-9cf6-1fda720bdb03"} 
    try:
        response = requests.delete(url + endpoint, json=data, stream=True)
        response.raise_for_status()  # Verifica se ocorreu algum erro na requisição

        data = response.json()  # Converte a resposta em formato JSON para um dicionário Python

     
        print(data)  # Exemplo: exibe a resposta da API

    except requests.exceptions.RequestException as e:
        print('Erro na requisição:', e)


consume()


