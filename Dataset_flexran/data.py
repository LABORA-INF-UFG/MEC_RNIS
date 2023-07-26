import pandas as pd
import requests

# Carregar o dataset
dataset = pd.read_csv('/l/disk0/mcunha/Documentos/ufg/MEC_RNIS/flexran/rni_d.csv')

# Iterar sobre as linhas do dataset
for _, row in dataset.iterrows():
    # Extrair as informações do dataset
    coluna1 = row['cell_user_info']
    coluna2 = row['request_id']
    coluna3 = row['time_stamp']
    # ...

    # Montar os dados a serem enviados na requisição POST
    data = {
        'coluna1': coluna1,
        'coluna2': coluna2,
        'coluna3': coluna3
        # ...
    }

    # Fazer a requisição POST para a API
    #Configurar o caminho do post
    response = requests.post('http://127.0.0.1:5000/tx/rni/v2/queries/teste/', json=data)

    # Verificar o status da resposta
    if response.status_code == 200:
        print('Dados enviados com sucesso para a API.')
    else:
        print('Erro ao enviar os dados para a API.')

