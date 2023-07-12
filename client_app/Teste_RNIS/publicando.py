import requests

def call_api():
    url = 'http://127.0.0.1:5000/rni/v2/queries/rab_info/2'  # URL da API

    
    try:
        response = requests.post(url, stream=True)
        response.raise_for_status()  # Verifica se ocorreu algum erro na requisição

        data = response.json()  # Converte a resposta em formato JSON para um dicionário Python

     
        print(data)  # Exemplo: exibe a resposta da API

    except requests.exceptions.RequestException as e:
        print('Erro na requisição:', e)

call_api()