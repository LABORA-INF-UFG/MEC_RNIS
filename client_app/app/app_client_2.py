
## Aplicação que utiliza da api do rnis e assina um topico "rab"

import requests

def call_api():
    url = 'http://127.0.0.1:5000/app_client/rni/v2'  # URL da API
    endpoint = '/subscriptions'  # Endpoint específico da API
    data = {"NotificationSubscription" : "rab"} 
    #data = {"NotificationSubscription" : "CellChangeSubscription"} 
    
    try:
        response = requests.post(url + endpoint, json=data)
        response.raise_for_status()  # Verifica se ocorreu algum erro na requisição

        data = response.json()  # Converte a resposta em formato JSON para um dicionário Python

        # Faça o processamento dos dados recebidos
        # ...

        #id_retorno = data['id']  # Supondo que a resposta JSON tenha um campo 'id'

        # Faça o armazenamento do ID de retorno da API
        # ...

        #print(f'ID de retorno da API: {id_retorno}')
        print(data)  # Exemplo: exibe a resposta da API

    except requests.exceptions.RequestException as e:
        print('Erro na requisição:', e)
    return data

call_api()