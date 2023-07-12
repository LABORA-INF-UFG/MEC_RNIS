import pika
import sqlite3, uuid, subprocess, os
from bd.table import create_table, insert_application, delete_application
from flask import Flask, Response, request, jsonify
from client_app.Teste_RNIS.subscription_controller2 import subscription_post
from v2.queries.rab_info_controller import RabInfo2, RabInfo1


from client_app.Teste_RNIS.exchange import Exchange


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

    #Exchange.stop_consumer()


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




# Rota principal que retorna as informações do RabbitMQ continuamente
@app.route('/rni/v2/queries/rab_info/2', methods=['POST'])
def pub():

    # Pega os dados enviados via post.
    dados = request.get_json()
    RabInfo1.post()
    result = Exchange.pub(dados)

    return result




# Função para verificar se a execução deve ser interrompida
def continue_running():
    return continue_running

# Rota para interromper a execução da API
@app.route('/stop')
def stop():
    global continue_running
    continue_running = False
    return 'API stopped'




if __name__ == '__main__':
     #print("Iniciando")
    
    os.chdir(diretorio) # Mudando para o diretório

    # Executando o comando docker para subir o RabbitMQ
    subprocess.run("docker-compose up -d", shell=True)
    
    print("RabbiMQ ok")
    
    os.chdir(current_directory) # Mudando para o diretório

    create_table() # Cria a tabela

    
    app.run(debug=True) # Executa a aplicação em modo debug

