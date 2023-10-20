from locust import HttpUser, task, between
import json
import pandas as pd

# Criaremos a classe ApiUser, que herda da classe HttpUser e nos dá a possibilidade de realizar requests do tipo HTTP. 
class ApiUser(HttpUser):
    
    #inserimos a informação do intervalo de tempo entre 1 e 3 segundos entre as requests enviadas.
    wait_time = between(6, 8)

    # Abra o arquivo JSON e leia os dados
    with open('radio_network_data.json', 'r') as file:
        data_list = json.load(file)


    # especificamos nossas tasks para os testes através do decorator @task 
    @task
    def send_data_to_api(self):
        # Se você deseja iterar sobre os dados do JSON em um loop, descomente a linha abaixo
        # for data in self.data_list:
        for data in self.data_list:
            # Realize uma solicitação POST para a API com os dados do JSON
            response = self.client.post('http://127.0.0.1:5000/rni/v2/queries/rab_info/1', json=data)
            # Verifique a resposta da API, se necessário
            if response.status_code == 200:
                print("API request successful")
            else:
                print(f"API request failed with status code: {response.status_code}")


    """ # especificamos nossas tasks para os testes através do decorator @task 
    @task
    def send_data_to_api_2(self):
        # Se você deseja iterar sobre os dados do JSON em um loop, descomente a linha abaixo
        # for data in self.data_list:
        for data in self.data_list:
            # Realize uma solicitação POST para a API com os dados do JSON
            response = self.client.post('http://127.0.0.1:5000/rni/v2/queries/rab_info/2', json=data)
            # Verifique a resposta da API, se necessário
            if response.status_code == 200:
                print("API request successful")
            else:
                print(f"API request failed with status code: {response.status_code}")

 """

    #Execute o comando locust -f locust_script.py -H http://127.0.0.1:5000 
    #e a interface gráfica deve aparecer no endereço http://127.0.0.1:8089/