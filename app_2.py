# Importando as bibliotecas
import sqlite3, uuid, subprocess, os

# from
from flask import Flask, jsonify, request
from flask_restful import Api
from bd.table import create_table, insert_application, delete_application
from v2.queries.rab_info_controller import RabInfo2
from v2.queries.plmn_info_controller import PlmnInfo2
from v2.queries.s1_bearer_info_controller import S1BearerInfo2 
from v2.subscription.subscription_controller2 import subscription_post

# Cria uma variavel para passar o Flask
app = Flask(__name__)

# Cria variaveis com o caminho das pastas
result = subprocess.run(['pwd'], capture_output=True, text=True)
current_directory = result.stdout.strip()
diretorio = f'{current_directory}/docker-compose'


# Configuração do banco de dados
DB_NAME = 'applications.db'

## Methods ##

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

    """ 
        Cada uma dos tipos de subscrições já devem estar cadastrados no Brocker, 
        Nesse ponto ao efetuar a requisição do tipo Post passando um NotificationSubscription eu devo
        vincular o appRoot a esse tipo de notificação ou seja inscrever esse appRoot no tópico do 
        NotificationSubscription especificado!
    """

    # A apiRoot que deve ter o código vinculado no banco de dados?
    # Obter o identificador da aplicação na requisição POST
    NotificationSubscription = request.json.get('NotificationSubscription')

    # Verificar se o identificador foi fornecido
    if not NotificationSubscription:
        return jsonify({'error': 'Identificador não fornecido'}), 400

    # Cadastrar a aplicação e obter o ID
    id = insert_application(appRoot)

    #Chama a função subscription_post
    t = subscription_post(NotificationSubscription) # Chama o subscription_post

    # Retornar o ID como resposta
    #return jsonify({'id': id, 'appRoot': appRoot, 'NotificationSubscription': NotificationSubscription, "t": t }), 200
    return t




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

# Resource: rab_info GET
@app.route('/<appRoot>/rni/v2/queries/rab_info', methods=['GET'])
def get_rab_info():
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})

# Resource: plmn_info GET
@app.route('/<appRoot>/rni/v2/queries/plmn_info ', methods=['GET'])
def get_plmn_info():
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})

# Resource: s1_bearer_info GET
@app.route('/<appRoot>/rni/v2/queries/s1_bearer_info ', methods=['GET'])
def get_s1_bearer_info():
   

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'sucesso'})

# Resource: layer2_meas GET
@app.route('/<appRoot>/rni/v2/queries/layer2_meas  ', methods=['GET'])
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

