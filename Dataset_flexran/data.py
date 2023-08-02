import pandas as pd
import requests

# Carregar o dataset
dataset = pd.read_csv('rni_d.csv')

# Iterar sobre as linhas do dataset
for _, row in dataset.iterrows():
    # Extrair as informações do dataset
    coluna1 = row['cell_user_info']
    coluna2 = row['request_id']
    coluna3 = row['time_stamp']
    # ...

    # Montar os dados a serem enviados na requisição POST
    data = {
        'cell_user_info': coluna1,
        'request_id': coluna2,
        'time_stamp': coluna3
        # ...
    }

    print ("data:", data)
    print ("data cell_user_info", data['cell_user_info'])

    # Fazer a requisição POST para a API
    #Configurar o caminho do post
    response = requests.post('http://127.0.0.1:5000/rni/v2/queries/rab_info/5', json=data)

    # Verificar o status da resposta
    if response.status_code == 200:
        print('Dados enviados com sucesso para a API.')
    else:
        print('Erro ao enviar os dados para a API.')

