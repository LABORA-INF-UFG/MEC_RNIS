from flask import Flask, request
import requests, json, time

# Variável global para contar as requisições
request_count = 0


app = Flask(__name__)


def post_registrer():
    api_url = 'http://127.0.0.1:5000/sdfe/rni/v2'  # Substitua pela URL da sua API
    endpoint = '/subscriptions'  # Endpoint específico da API
    callback_uri = 'http://localhost:8009/callback3'  # URL do callback para receber notificações

    data = {
        'NotificationSubscription': "plmn",
        'callback_uri': "http://localhost:8009/callback3"
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
@app.route('/callback3', methods=['POST'])
def callback():
    global request_count  # Usar a variável global

    data = request.json  # Dados recebidos na notificação
    request_count += 1  # Incrementar a contagem de requisições

    # Processar os dados recebidos da notificação
    print('Received notification:')
    start_time_str, message = data.split(':', 1)
    start_time = float(start_time_str)
    
    # Calcule o tempo de entrega
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    data = {'message': message}

    # Especifique o caminho completo para o arquivo "tempos.txt"
    caminho_arquivo = "/l/disk0/mcunha/Documentos/ufg/MEC_RNIS/locust/20_minutos_client_200users_1s_2_mec_apps/tempos_decorridos_plmn_client_2.txt"

    with open(caminho_arquivo, "a") as arquivo:
        arquivo.write(f"{elapsed_time}\n")
    
    return 'Notification received', 200 


if __name__ == '__main__':

    post_registrer()
        
    app.run(host='0.0.0.0', port=8009)