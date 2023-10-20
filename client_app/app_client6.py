from flask import Flask, request
import requests, json

# Variável global para contar as requisições
request_count = 0

app = Flask(__name__)


def post_registrer():
    api_url = 'http://127.0.0.1:5000/app_6/rni/v2'  # Substitua pela URL da sua API
    endpoint = '/subscriptions'  # Endpoint específico da API
    preferences = ['notification_type_1', 'notification_type_2']  # As preferências de notificação do cliente
    callback_uri = 'http://localhost:8004/callback_app_6'  # URL do callback para receber notificações

    data = {
        'NotificationSubscription': "rab",
        'callback_uri': "http://localhost:8004/callback_app_6"
    }

    try:
        response = requests.post(api_url + endpoint, json=data, stream=True)
        
        if response.status_code == 200:
            print(f'Client app_teste registered successfully with callback URL {callback_uri}.')
                # Iterar sobre as informações recebidas
            for data in response.iter_lines():
                if data:
                    # Decodificar o JSON recebido
                    json_data = data.decode('utf-8')
                    #print("Teste")
                    print(json_data)  # Exibir as informações na tela
        else:
            print(f'Error: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'Error: {str(e)}')


#http://localhost:8000/callback_app_ciente
@app.route('/callback_app_6', methods=['POST'])
def callback():
    global request_count  # Usar a variável global
    
    data = request.json  # Dados recebidos na notificação
    request_count += 1  # Incrementar a contagem de requisições

    # Processar os dados recebidos da notificação
    print('Received notification:')
    print(data)

    # Atualizar o arquivo JSON com a contagem de requisições
    with open('60_minutos_rab_1000_users_1_2_segundos_dataset_6.json', 'w') as file:
        json.dump({'request_count': request_count}, file)
    return 'Notification received', 200


if __name__ == '__main__':

    post_registrer()
        
    app.run(host='0.0.0.0', port=8004)