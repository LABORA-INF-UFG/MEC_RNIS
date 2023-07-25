import requests

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
