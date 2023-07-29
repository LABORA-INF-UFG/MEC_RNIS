from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def send_data_to_api(self):
        # Dados para enviar na requisição POST
        data = {
            "key1": "value1",
            "key2": "value2"
            # Adicione aqui os dados que deseja enviar para a API
        }

        # Enviar a requisição POST para a API
        response = self.client.post("http://127.0.0.1:5000/api/receber-dados", json=data)

        # Exibir o status da resposta (opcional)
        print(f"Status da resposta: {response.status_code}")
        print(f"Resposta: {response.text}")

