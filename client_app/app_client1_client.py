from flask import Flask, request
import requests
import json
import time
import argparse
import os
import subprocess

# Variável global para contar as requisições
request_count = 0

app = Flask(__name__)

def post_registrer():
    api_url = 'http://127.0.0.1:5000/app_1/rni/v2'
    endpoint = '/subscriptions'
    preferences = ['notification_type_1', 'notification_type_2']
    callback_uri = 'http://localhost:8001/callback_app_1'

    data = {
        'NotificationSubscription': "plmn",
        'callback_uri': callback_uri
    }

    try:
        response = requests.post(api_url + endpoint, json=data, stream=True)
        
        if response.status_code == 200:
            print(f'Client app_teste registered successfully with callback URL {callback_uri}.')
            for data in response.iter_lines():
                if data:
                    json_data = data.decode('utf-8')
                    print(json_data)
        else:
            print(f'Error: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'Error: {str(e)}')

@app.route('/callback_app_1', methods=['POST'])
def callback():
    global request_count

    data = request.json

    print('Received notification:')

    start_time_str, message = data.split(':', 1)
    start_time = float(start_time_str)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    data = {'message': message}

    n = args.n if args.n else ""  # Adicione o número ao nome do arquivo se fornecido

    caminho_arquivo = os.path.join(args.directory, f"tempos_decorridos_plmn_app1_client_{n}.txt")

    with open(caminho_arquivo, "a") as arquivo:
        arquivo.write(f"{elapsed_time}\n")

    return 'Notification received', 200

if __name__ == '__main__':

        # Obter o caminho do diretório atual
    result = subprocess.run(['pwd'], capture_output=True, text=True)
    current_directory = result.stdout.strip()

    # Voltar um nível para o diretório pai
    parent_directory = subprocess.run(['dirname', current_directory], capture_output=True, text=True)
    parent_directory = parent_directory.stdout.strip()

    print("caminho" + parent_directory)

    parser = argparse.ArgumentParser(description='Flask app for handling notifications and writing to a file.')
    parser.add_argument('--directory', type=str, default= current_directory + "/locust/10_minutos_client_100users_1s_2_mec_apps/", help='Diretório onde o arquivo está localizado.')
    parser.add_argument('--n', type=int, default=None, help='Número para adicionar ao nome do arquivo.')
    args = parser.parse_args()

    post_registrer()
    app.run(host='0.0.0.0', port=8001)