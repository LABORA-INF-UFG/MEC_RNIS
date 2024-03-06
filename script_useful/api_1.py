# Importando as bibliotecas
import sqlite3, uuid, subprocess, os, requests, pika
import requests

# from
from flask import Flask, jsonify, request
from flask_restful import Api
import threading
from bd.table import create_table, insert_application, delete_application
from v2.queries.rab_info_controller import RabInfo2, RabInfo1
from v2.queries.plmn_info_controller import PlmnInfo
from v2.queries.s1_bearer_info_controller import S1BearerInfo2 
from v2.subscription.subscription_controller import subscription_verification
from v2.receive.exchange import Exchange

# Cria uma variavel para passar o Flask
app = Flask(__name__)

# Cria variaveis com o caminho das pastas
result = subprocess.run(['pwd'], capture_output=True, text=True)
current_directory = result.stdout.strip()
diretorio = f'{current_directory}/docker-compose'

# Configuração do banco de dados
DB_NAME = 'applications.db'

## Methods ##

#################################################################

# Resource: Subscription GET
@app.route('/<appRoot>/rni/v2/subscriptions', methods=['GET'])
def get_application_route():
    # Obter o ID da aplicação a ser excluída na requisição POST
    subscription_type = request.json.get('subscription_type')

    # Verificar se o ID foi fornecido
    if not subscription_type:
        data = {
                "subscription_type": "subscription_type não fornecido",
                 "status": 400
        }
        return jsonify(data), 400
            
    # Retornar uma resposta de sucesso
    return jsonify({'subscription_type': subscription_type,  'SubscriptionLinkList' : 'Após o sucesso, um corpo de resposta contendo a lista de links para as assinaturas do solicitante é retornado.'}), 200


# Resource: Subscription POST
@app.route('/<appRoot>/rni/v2/subscriptions', methods=['POST'])
def register_application(appRoot):
     
    try:
        NotificationSubscription = request.json.get('NotificationSubscription')
        callback_uri = request.json.get('callback_uri')

        if not NotificationSubscription:
            return jsonify({'error': 'Client NotificationSubscription not provided'}), 400

        if 'nok' == subscription_verification(NotificationSubscription):
            return jsonify({'error': 'Invalid NotificationSubscription'}), 400

        if not callback_uri:
            return jsonify({'error': 'Client callback_uri not provided'}), 400
        
          # Cadastrar a aplicação e obter o ID
        id = insert_application(appRoot, NotificationSubscription, callback_uri)

        return jsonify({'NotificationSubscription': NotificationSubscription, 'callback': callback_uri, 'id_registre': id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Resource: Subscription DELETE
@app.route('/<appRoot>/rni/v2/subscriptions', methods=['DELETE'])
def delete_application_route(appRoot):
    # Obter o ID da aplicação a ser excluída na requisição POST
    id = request.json.get('id')

    # Verificar se o ID foi fornecido
    if not id:
        return jsonify({'error': 'ID não fornecido'}), 400

    # Excluir a aplicação com o ID fornecido
    delete_application(id)

    result = Exchange.stop()


    # Retornar uma resposta de sucesso
    return jsonify({'message': 'ID excluído com sucesso'}), 200


# Resource: SubscriptionsID GET
@app.route('/<appRoot>/rni/v2/subscriptions/<subscriptionId>', methods=['GET'])
def get_subscriptionId(appRoot, subscriptionId):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': subscriptionId})


# Resource: SubscriptionsID PUT
@app.route('/<appRoot>/rni/v2/subscriptions/<subscriptionId>', methods=['PUT'])
def put_subscriptionId(appRoot, subscriptionId):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})


# Resource: SubscriptionsID DELETE
@app.route('/<appRoot>/rni/v2/subscriptions/<subscriptionId>', methods=['DELETE'])
def delete_subscriptionId(appRoot, subscriptionId):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})


#################################################################


# Resource: rab_info GET
@app.route('/<appRoot>/rni/v2/queries/rab_info/<app_ins_id>', methods=['GET'])
def get_rab_info(appRoot, app_ins_id ):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': appRoot, 'teste': app_ins_id })



# Resource: plmn_info GET
@app.route('/<appRoot>/rni/v2/queries/plmn_info/<app_ins_id>', methods=['GET'])
def get_plmn_info(appRoot, app_ins_id):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})



# Resource: s1_bearer_info GET
@app.route('/<appRoot>/rni/v2/queries/s1_bearer_info/<app_ins_id>', methods=['GET'])
def get_s1_bearer_info(appRoot, app_ins_id):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})



# Resource: layer2_meas GET
@app.route('/<appRoot>/rni/v2/queries/layer2_meas/<app_ins_id>', methods=['GET'])
def get_layer2_meas (appRoot, app_ins_id):
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})


#################################################################


# Criar outra variavel para passar o app
api = Api(app)

# Resource: rab_info POST
api.add_resource(RabInfo1, '/rni/v2/queries/rab_info/<string:app_instance_id>')
api.add_resource(PlmnInfo, '/rni/v2/queries/plmn_info/<string:app_instance_id>')
api.add_resource(S1BearerInfo2, '/rni/v2/queries/s1_bearer_info')

## Main ##

# Configuração basica do Flask
if __name__ == '__main__':

    os.chdir(diretorio) # Mudando para o diretório
    # Executando o comando docker para subir o RabbitMQ
    subprocess.run("docker-compose up -d", shell=True)
    os.chdir(current_directory) # Mudando para o diretório

    create_table() # Cria a tabela

    app.run(port=5000)
    #app.run() # Executa a aplicação em modo debug
   

# Running on http://127.0.0.1:5000/rni/v2/queries/rab_info
#python3 app.py