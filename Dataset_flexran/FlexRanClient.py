import requests
from flexran import FlexRANClient

# Criação de uma instância do cliente FlexRAN
flexran_client = FlexRANClient()

# Configuração do FlexRAN e obtenção das informações de rádio
def get_radio_info():
    # Configurar o FlexRAN para obter as informações relevantes de rádio
    # Por exemplo, definir os parâmetros de monitoramento desejados

    # Obter as informações de rádio
    radio_info = flexran_client.get_radio_info()

    return radio_info

# Função para enviar as informações de rádio para sua API
def send_radio_info_to_api(radio_info):
    # URL da sua API para enviar as informações
    api_url = 'http://localhost:5000/api/radio'

    try:
        response = requests.post(api_url, json=radio_info)
        response.raise_for_status()  # Verifica se ocorreu algum erro na requisição

        # Verifica a resposta da API, se necessário
        print(response.json())

    except requests.exceptions.RequestException as e:
        print('Erro na requisição:', e)

# Obtém as informações de rádio
radio_info = get_radio_info()

# Envia as informações de rádio para sua API
send_radio_info_to_api(radio_info)
