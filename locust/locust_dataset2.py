from locust import HttpUser, task, between
import pandas as pd
import json

class MyUser(HttpUser):
    wait_time = between(1, 3)

    def load_data(self):
        # Ler o arquivo CSV com os dados para a requisição POST
        dataset = pd.read_csv('/home/kaique/Documentos/ufg/MEC_RNIS/locust/rni_d.csv')
        return dataset

    @task
    def post_data(self):
        # Carregar os dados do dataset
        dataset = self.load_data()

        for _, data in dataset.iterrows():
            json_data = json.dumps(data.to_dict())
            headers = {'Content-Type': 'application/json'}
            response = self.client.post("http://127.0.0.1:5000/rni/v2/queries/rab_info/3", data=json_data, headers=headers)
            print("Status da resposta (POST):", response.status_code)
