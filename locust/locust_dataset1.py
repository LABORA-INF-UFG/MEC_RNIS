from locust import HttpUser, task, between
import pandas as pd

# Criaremos a classe ApiUser, que herda da classe HttpUser e nos dá a possibilidade de realizar requests do tipo HTTP. 
class ApiUser(HttpUser):
    
    #inserimos a informação do intervalo de tempo entre 1 e 3 segundos entre as requests enviadas.
    wait_time = between(1, 3)

    
    @task
    def send_data_to_api_3_dataset(self):
        # Dados para enviar na requisição POST
        # Dados que vamos enviar para a API
        # Carregar o dataset
        dataset = pd.read_csv('/home/kaique/Documentos/ufg/MEC_RNIS/locust/rni_d.csv')

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


        # Enviar a requisição POST para a API
        response = self.client.post("http://127.0.0.1:5000/rni/v2/queries/rab_info/3", json=data)

        # Exibir o status da resposta (opcional)
        print(f"Status da resposta 2: {response.status_code}")
        print(f"Resposta 2: {response.text}")

    #Execute o comando locust -f locust_script.py -H http://127.0.0.1:5000 
    #e a interface gráfica deve aparecer no endereço http://127.0.0.1:8089/