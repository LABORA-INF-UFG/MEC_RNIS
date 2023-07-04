import json
from flask import Flask, Response

app = Flask(__name__)

# Variável global para verificar se a API deve continuar retornando informações
continue_running = True

# Rota principal que retorna as informações continuamente
@app.route('/continuous-data')
def generate_data():
    counter = 0

    def generate():
        nonlocal counter
        while True:
            data = {'data': counter}
            json_data = json.dumps(data) + '\n'
            yield json_data.encode('utf-8')
            counter += 1

    return Response(generate(), mimetype='application/json')



# Rota para interromper a execução da API
@app.route('/stop')
def stop():
    global continue_running
    continue_running = False
    return 'API stopped'

if __name__ == '__main__':
    app.run()


