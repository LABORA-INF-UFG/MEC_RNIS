# Importando as bibliotecas
import sqlite3, uuid, subprocess, os


from flask import Flask, jsonify, request
from flask_restful import Api
from bd.table import create_table, insert_application, delete_application
from v2.queries.rab_info_controller import RabInfo2
from v2.queries.plmn_info_controller import PlmnInfo2
from v2.queries.s1_bearer_info_controller import S1BearerInfo2 
from v2.subscription.subscription_controller import subscription_post


# Cria uma variavel para passar o Flask
app = Flask(__name__)

# Cria variaveis com o caminho das pastas
result = subprocess.run(['pwd'], capture_output=True, text=True)
current_directory = result.stdout.strip()
diretorio = f'{current_directory}/docker-compose'


# Configuração do banco de dados
DB_NAME = 'applications.db'

## Methods ##

# Subscription POST
@app.route('/rni/v2/subscription/subscriptions', methods=['POST'])
def register_application():
    # Obter o identificador da aplicação na requisição POST
    NotificationSubscription = request.json.get('NotificationSubscription')

    # Verificar se o identificador foi fornecido
    if not NotificationSubscription:
        return jsonify({'error': 'Identificador não fornecido'}), 400

    # Cadastrar a aplicação e obter o ID
    id = insert_application(NotificationSubscription)

    # Retornar o ID como resposta
    return jsonify({'id': id}), 200

# Subscription DELETE
@app.route('/rni/v2/subscription/subscriptions', methods=['DELETE'])
def delete_application_route():
    # Obter o ID da aplicação a ser excluída na requisição POST
    id = request.json.get('id')

    # Verificar se o ID foi fornecido
    if not id:
        return jsonify({'error': 'ID não fornecido'}), 400

    # Excluir a aplicação com o ID fornecido
    delete_application(id)

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'ID excluído com sucesso'}), 200


# SubscriptionsID GET
@app.route('/rni/v2/queries/subscriptions/<subscriptionId>', methods=['GET'])
def get_subscriptionId(subscriptionId):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': subscriptionId})



# SubscriptionsID DELETE
@app.route('/rni/v2/queries/subscriptions/<subscriptionId>', methods=['DELETE'])
def delete_subscriptionId(subscriptionId):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})

# SubscriptionsID PUT
@app.route('/rni/v2/queries/subscriptions/<subscriptionId>', methods=['PUT'])
def put_subscriptionId(subscriptionId):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})



#
@app.route('/rni/v2/queries/rab_info', methods=['GET'])
def get_rab_info():
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})


#
@app.route('/rni/v2/queries/plmn_info ', methods=['GET'])
def get_plmn_info():
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})

#
@app.route('/rni/v2/queries/s1_bearer_info ', methods=['GET'])
def get_s1_bearer_info():
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})

#
@app.route('/rni/v2/queries/layer2_meas  ', methods=['GET'])
def get_layer2_meas ():
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})


## Main ##

# Configuração basica do Flask
if __name__ == '__main__':

    #print("Iniciando")
    
    os.chdir(diretorio) # Mudando para o diretório

    # Executando o comando docker para subir o RabbitMQ
    subprocess.run("docker-compose up -d", shell=True)
    
    #print("RabbiMQ ok")
    
    os.chdir(current_directory) # Mudando para o diretório

    create_table() # Cria a tabela

    
    app.run(debug=True) # Executa a aplicação em modo debug
    #app.run() # Executa a aplicação

# Running on http://127.0.0.1:5000/rni/v2/queries/rab_info
#python3 app.py

