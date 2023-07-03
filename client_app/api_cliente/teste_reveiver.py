## Apei que recebe as informações do RNIS

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/api/receive', methods=['POST'])
def receive_message():
    message = request.get_json()
    
    # Processar a mensagem recebida
    # ...
    print ("menssage: ", message)
    return 'Mensagem recebida com sucesso!'

if __name__ == '__main__':
    app.run(port=5001)