import requests

url = 'http://localhost:5000/continuous-data'

# Fazer a requisição GET para receber as informações continuamente
response = requests.get(url, stream=True)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Iterar sobre as informações recebidas
    for data in response.iter_lines():
        if data:
            # Decodificar o JSON recebido
            json_data = data.decode('utf-8')
            #print("Teste")
            print(json_data)  # Exibir as informações na tela
else:
    print('Erro na requisição:', response.status_code)
