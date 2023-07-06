
## Aplicação que utiliza da api do rnis e assina um topico "rab"

import requests

def call_api():
    url = 'http://127.0.0.1:5000/app_client/rni/v2'  # URL da API
    endpoint = '/subscriptions'  # Endpoint específico da API
    data = {"NotificationSubscription" : "rab"} 
    #data = {"NotificationSubscription" : "CellChangeSubscription"} 
    
    try:
        response = requests.post(url + endpoint, json=data)
        

        if response.status_code == 200:
            # Iterar sobre as informações recebidas
            #for data in response.iter_lines():
            #    if data:
                    # Decodificar o JSON recebido
                    #json_data = data.decode('utf-8')
                    data1 = response.json()
                    print(data1)  # Exibir as informações na tela

    except requests.exceptions.RequestException as e:
        print('Erro na requisição:', e)
    return data

call_api()