from locust import HttpUser, task, between

class ApiUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def send_data_to_api(self):
        # Dados para enviar na requisição POST
        data = {
                "cell_user_info": {
                    "ecgi": {
                        "cell_id":  "1",
                        "plmn" :{
                            "mcc" : "mcc",
                            "mnc" : "mnc"
                        }
                    },
                    "ue_info": {
                        "associate_id": {
                            "type": "1",
                            "value": "constante"
                        },
                        "erab_info": {
                            "erab_id": 14,
                            "erab_qos_parameters": {
                                "qci": 1,
                                "qos_information": {
                                    "erab_gbr_dl": 1,
                                    "erab_gbr_ul": 1,
                                    "erab_mbr_dl": 1,
                                    "erab_mbr_ul": 1
                                }
                            }
                        }
                    }
                },
                "request_id": "1",
                "time_stamp": {
                    "nano_seconds": 12,
                    "seconds": 13
                }
            }
            # Adicione aqui os dados que deseja enviar para a API

        # Enviar a requisição POST para a API
        response = self.client.post("http://127.0.0.1:5000/rni/v2/queries/rab_info/1", json=data)

        # Exibir o status da resposta (opcional)
        print(f"Status da resposta: {response.status_code}")
        print(f"Resposta: {response.text}")

