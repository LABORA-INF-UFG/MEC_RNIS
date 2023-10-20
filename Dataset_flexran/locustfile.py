from locust import HttpUser, task, between
import csv

class MyLocustUser(HttpUser):
    wait_time = between(1, 5)  # Tempo de espera entre as solicitações

    # Abra o arquivo CSV e leia os dados
    with open('radio_network_data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        data_list = list(csv_reader)

    # Defina as tarefas que o usuário realizará
    @task(1)
    def send_data_to_api(self):
        # Se você deseja iterar sobre os dados do CSV em um loop, descomente a linha abaixo
        # for data in self.data_list:
        for data in self.data_list:

            # Realize uma solicitação POST para a API com os dados do CSV
            response = self.client.post('http://127.0.0.1:5000/rni/v2/queries/rab_info/1', json=data)
            # Verifique a resposta da API, se necessário
            if response.status_code == 200:
                print("API request successful")
                print (data)
            else:
                print(f"API request failed with status code: {response.status_code}")
                print (data)