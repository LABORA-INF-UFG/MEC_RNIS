import requests

url = 'http://localhost:5000/api/id'  # Altere a URL para corresponder ao endpoint da sua API

response = requests.post(url)
data = response.json()

if response.status_code == 200:
    id = data['id']
    print(f'Recebido o ID: {id}')
else:
    print('Erro ao enviar a solicitação POST')