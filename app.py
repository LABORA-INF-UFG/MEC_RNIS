# rni_simples
#pip3 install Flask
#pip3 install Flask-Restful
#pip3 install connexion
#pip3 install pika

# Importando as bibliotecas
import subprocess
import os


from flask import Flask
from flask_restful import Api
from v2.queries.rab_info_controller import RabInfo2
from v2.queries.plmn_info_controller import PlmnInfo2
from v2.queries.s1_bearer_info_controller import S1BearerInfo2 
from v2.subscription.subscription_controller import subscription_post


result = subprocess.run(['pwd'], capture_output=True, text=True)
current_directory = result.stdout.strip()

diretorio = f'{current_directory}/docker-compose'

# Cria uma variavel para passar o Flask
app = Flask(__name__)

# Criar outra variavel para passar o app
api = Api(app)


# Adicionar os recursos
#api.add_resource(RabInfo, '/rni/v2/queries/rab_info')
#api.add_resource(PlmnInfo, '/rni/v2/queries/plmn_info')
#api.add_resource(S1BearerInfo, '/rni/v2/queries/s1_bearer_info')

api.add_resource(RabInfo2, '/rni/v2/queries/rab_info/<string:app_instance_id>')
api.add_resource(PlmnInfo2, '/rni/v2/queries/plmn_info/<string:app_instance_id>')
api.add_resource(S1BearerInfo2, '/rni/v2/queries/s1_bearer_info')
api.add_resource(subscription_post, '/rni/v2/subscription/subscription/<string:exchange_name>,<string:queue_name>,<string:severity>')
# api.add_resource(subscription_post, '/rni/v2/subscription/subscriptions')

# Configuração basica do Flask
if __name__ == '__main__':

    
    print("Iniciando")
    os.chdir(diretorio) # Mudando para o diretório
    #Executando o comando docker para subir o RabbitMQ
    subprocess.run("docker-compose up -d", shell=True)
    print("RabbiMQ ok")
    os.chdir(current_directory) # Mudando para o diretório
    app.run(debug=True)
    

# Running on http://127.0.0.1:5000/rni/v2/queries/rab_info
#http://127.0.0.1:5000/hoteis
#python3 app.py
