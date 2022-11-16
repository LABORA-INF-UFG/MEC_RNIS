# rni_simples
#pip3 install Flask
#pip3 install Flask-Restful
#pip3 install connexion
#pip3 install pika

# Importando as bibliotecas

from flask import Flask
from flask_restful import Api
from v2.queries.rab_info_controller import RabInfo, RabInfo2
#from v2.queries.plmn_info_controller import PlmnInfo, PlmnInfo2
#from v2.queries.s1bearer_info_controller import S1BearerInfo


# Cria uma variavel para passar o Flask
app = Flask(__name__)

# Criar outra variavel para passar o app
api = Api(app)


# Adicionar os recursos
api.add_resource(RabInfo2, '/rni/v2/queries/rab_info/<string:app_instance_id>')
api.add_resource(RabInfo, '/rni/v2/queries/rab_info')
#api.add_resource(PlmnInfo2, '/rni/v2/queries/plmn_info/<string:app_instance_id>')
#api.add_resource(PlmnInfo, '/rni/v2/queries/plmn_info')
#api.add_resource(S1BearerInfo, '/rni/v2/queries/s1_bearer_info/<string:app_instance_id>')

# Configuração basica do Flask
if __name__ == '__main__':
    app.run(debug=True)

# Running on http://127.0.0.1:5000/rni/v2/queries/rab_info
#http://127.0.0.1:5000/hoteis
#python3 app.py
