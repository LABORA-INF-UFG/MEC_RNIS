import pika
import sqlite3, uuid, subprocess, os
from bd.table import create_table, insert_application, delete_application
from flask import Flask, Response, request, jsonify
from client_app.Teste_RNIS.subscription_controller2 import subscription_post


from client_app.Teste_RNIS.exchange import Exchange


app = Flask(__name__)

# Rota principal que retorna as informações do RabbitMQ continuamente
@app.route('/<appRoot>/rni/v2/subscriptions', methods=['POST'])
def register_application(appRoot):

    NotificationSubscription = request.json.get('NotificationSubscription')

    if not NotificationSubscription:
        return jsonify({'error': 'Identificador não fornecido'}), 400

    id = insert_application(appRoot)

    #Chama a função subscription_post
    result = subscription_post(NotificationSubscription) # Chama o subscription_post

    return result


# Rota principal que retorna as informações do RabbitMQ continuamente
@app.route('/rni/v2/pub', methods=['POST'])
def pub():

    result = Exchange.pub()

  
    return result, 200

# Função para verificar se a execução deve ser interrompida
def continue_running():
    return continue_running

# Rota para interromper a execução da API
@app.route('/stop')
def stop():
    global continue_running
    continue_running = False
    return 'API stopped'


# Cria variaveis com o caminho das pastas
result = subprocess.run(['pwd'], capture_output=True, text=True)
current_directory = result.stdout.strip()
diretorio = f'{current_directory}/docker-compose'

if __name__ == '__main__':
     #print("Iniciando")
    
    os.chdir(diretorio) # Mudando para o diretório

    # Executando o comando docker para subir o RabbitMQ
    subprocess.run("docker-compose up -d", shell=True)
    
    print("RabbiMQ ok")
    
    os.chdir(current_directory) # Mudando para o diretório

    create_table() # Cria a tabela

    
    app.run(debug=True) # Executa a aplicação em modo debug

