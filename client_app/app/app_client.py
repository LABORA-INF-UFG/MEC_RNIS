import requests

def call_api():
    url = 'http://127.0.0.1:5000/app_client/rni/v2'  # URL da API
    endpoint = '/subscriptions'  # Endpoint específico da API
    data = {"NotificationSubscription" : "CellChangeSubscription"} 
    
    try:
        response = requests.post(url + endpoint, json=data)
        response.raise_for_status()  # Verifica se ocorreu algum erro na requisição

        data = response.json()  # Converte a resposta em formato JSON para um dicionário Python

     
        print(data)  # Exemplo: exibe a resposta da API

    except requests.exceptions.RequestException as e:
        print('Erro na requisição:', e)

call_api()