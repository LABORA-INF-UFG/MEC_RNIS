from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/endpoint', methods=['GET', 'POST'])
def endpoint_proxy():
    # Encaminhar a requisição para a API de destino
    url1 = 'http://127.0.0.1:5000/'
    url2 = '/rni/v2/subscriptions'
    url3 = url1 + 'tx' + url2
    headers = {'Content-Type': 'application/json'}
    data = request.json  # Dados da requisição recebidos na API atual

    # Realizar a requisição para a API de destino
    response = requests.request(request.method, url3, headers=headers, json=data)

    # Retornar a resposta da API de destino para o cliente
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run()