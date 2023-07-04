import requests

def stop_processing():
    # Enviar uma requisição GET para solicitar a finalização do processamento
    response = requests.get('http://localhost:5000/api/process?action=stop')
    response.raise_for_status()  # Verificar se ocorreu algum erro na requisição

    print('Solicitação de finalização enviada.')


def start_processing():
    # Dados a serem processados
    data = {
        'key1': 'value1',
        'key2': 'value2'
    }

    # Enviar a requisição POST para iniciar o processamento
    response = requests.post('http://localhost:5000/api/process', json=data)
    response.raise_for_status()  # Verificar se ocorreu algum erro na requisição

    print('Processamento iniciado.')

    # Continuar processando até solicitar a finalização
    while True:
        action = input('Digite "stop" para finalizar o processamento: ')
        #action = 'start'
        ##pegar a resposta e postar aqui
        if action.lower() == 'stop':
            # Enviar uma requisição GET para solicitar a finalização
            response = requests.get('http://localhost:5000/api/process?action=stop')
            response.raise_for_status()  # Verificar se ocorreu algum erro na requisição

            print('Processamento finalizado.')
            break

if __name__ == '__main__':
    start_processing(),
#    stop_processing()

