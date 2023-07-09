import pika
from flask import Flask, Response
from subscription_controller2 import subscription_post
from exchange import Exchange

app = Flask(__name__)

# Rota principal que retorna as informações do RabbitMQ continuamente
@app.route('/continuous-data')
def continuous_data():

    NotificationSubscription = "rab"
        #Chama a função subscription_post
    result = subscription_post(NotificationSubscription) # Chama o subscription_post


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
    app.run()
