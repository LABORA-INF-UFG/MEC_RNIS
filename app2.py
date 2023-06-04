# rni_simples
#pip3 install Flask
#pip3 install Flask-Restful
#pip3 install connexion
#pip3 install pika

# Importando as bibliotecas
import subprocess
import os


from flask import Flask, jsonify
from flask_restful import Api
from v2.queries.rab_info_controller import RabInfo2
from v2.queries.plmn_info_controller import PlmnInfo2
from v2.queries.s1_bearer_info_controller import S1BearerInfo2 
from v2.subscription.subscription_controller import subscription_post


# Cria uma variavel para passar o Flask
app = Flask(__name__)
ids = []
next_id = 1

@app.route('/rni/v2/queries/rab_info', methods=['POST'])
def generate_id():
    global next_id
    new_id = next_id
    next_id += 1
    ids.append(new_id)
    return jsonify({'id': new_id})

@app.route('/rni/v2/queries//plmn_info', methods=['POST'])
def generate_id_2():
    global next_id
    new_id = next_id
    next_id += 1
    ids.append(new_id)
    return jsonify({'id': "new_id"})

# Configuração basica do Flask
if __name__ == '__main__':
    app.run()
