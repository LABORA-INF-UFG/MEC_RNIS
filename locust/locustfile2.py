from locust import HttpUser, task, between
import json

class MyLocustUser(HttpUser):
    wait_time = between(1, 2)  # Tempo de espera entre as solicitações

    # Abra o arquivo JSON e leia os dados
    with open('radio_network_data_rab.json', 'r') as file:
        data_list_rab = json.load(file)

    # Abra o arquivo JSON e leia os dados
    with open('radio_network_data_plmn.json', 'r') as file:
        data_list_plmn = json.load(file)

    # Defina as tarefas que o usuário realizará
    @task(1)
    def send_data_to_api(self):
        # Se você deseja iterar sobre os dados do JSON em um loop, descomente a linha abaixo
        # for data in self.data_list:
        for data in self.data_list_rab:
            # Realize uma solicitação POST para a API com os dados do JSON
            response = self.client.post('http://127.0.0.1:5000/rni/v2/queries/rab_info/1', json=data)
            # Verifique a resposta da API, se necessário
            if response.status_code == 200:
                print("API request successful")
            else:
                print(f"API request failed with status code: {response.status_code}")

# Defina as tarefas que o usuário realizará
    @task(2)
    def send_data_to_api_2(self):
        # Se você deseja iterar sobre os dados do JSON em um loop, descomente a linha abaixo
        # for data in self.data_list:
        for data in self.data_list_plmn:
            # Realize uma solicitação POST para a API com os dados do JSON
            response = self.client.post('http://127.0.0.1:5000/rni/v2/queries/plmn_info/1', json=data)
            # Verifique a resposta da API, se necessário
            if response.status_code == 200:
                print("API request successful")
            else:
                print(f"API request failed with status code: {response.status_code}")
