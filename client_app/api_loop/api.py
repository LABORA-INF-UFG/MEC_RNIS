from flask import Flask, request

app = Flask(__name__)

@app.route('/api/process', methods=['POST'])
def process_request():
    # Receber os dados da requisição
    data = request.json

    # Processar os dados conforme necessário
    # ...

    while True:
        # Verificar se o cliente solicitou a finalização
        if request.args.get('action') == 'stop':
            break
        return "aqui"
        # Continuar processando os dados ou executando tarefas

    return 'Processamento finalizado'


if __name__ == '__main__':
    app.run()
