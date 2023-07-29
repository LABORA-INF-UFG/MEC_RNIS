from flask import Flask, request

app = Flask(__name__)

@app.route('/api/receber-dados', methods=['POST'])
def receber_dados():
    if request.method == 'POST':
        data = request.get_json()  # Recebe os dados enviados no corpo da requisição em formato JSON
        # Faça o processamento dos dados recebidos, se necessário
        # ...

        # Exemplo: imprimir os dados no terminal
        print("Dados recebidos:")
        print(data)

        return 'Requisição POST recebida com sucesso!', 200

    return "Método não permitido.", 405

if __name__ == '__main__':
    app.run()
