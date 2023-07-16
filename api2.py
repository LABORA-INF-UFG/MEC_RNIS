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
 
    result = Exchange.stop()

    # Retornar uma resposta de sucesso
    return jsonify({'message': 'ID excluído com sucesso'}), 200




# Rota principal que retorna as informações do RabbitMQ continuamente
@app.route('/rni/v2/queries/rab_info/<app_instance_id>', methods=['POST'])
def pub(app_instance_id):

    # Pega os dados enviados via post.
    dados = request.get_json()
    result2 =RabInfo1.post(app_instance_id, dados)
    #result = Exchange.pub(dados)

    return result2








if __name__ == '__main__':
     #print("Iniciando")
    
    os.chdir(diretorio) # Mudando para o diretório

    # Executando o comando docker para subir o RabbitMQ
    subprocess.run("docker-compose up -d", shell=True)
    
    print("RabbiMQ ok")
    
    os.chdir(current_directory) # Mudando para o diretório

    create_table() # Cria a tabela

    
    app.run(debug=True) # Executa a aplicação em modo debug

