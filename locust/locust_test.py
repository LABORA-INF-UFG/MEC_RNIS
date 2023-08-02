from locust import HttpUser, task, between
import pandas as pd

# Criaremos a classe ApiUser, que herda da classe HttpUser e nos dá a possibilidade de realizar requests do tipo HTTP. 
class ApiUser(HttpUser):
    
    #inserimos a informação do intervalo de tempo entre 1 e 3 segundos entre as requests enviadas.
    wait_time = between(1, 3)

    # especificamos nossas tasks para os testes através do decorator @task 
    @task
    def send_data_to_api(self):
        # Dados para enviar na requisição POST
        # Dados que vamos enviar para a API
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
            
        # Enviar a requisição POST para a API
        response = self.client.post("http://127.0.0.1:5000/rni/v2/queries/rab_info/1", json=data)

        # Exibir o status da resposta (opcional)
        print(f"Status da resposta 1: {response.status_code}")
        print(f"Resposta 1: {response.text}")

    # especificamos nossas tasks para os testes através do decorator @task 
    @task
    def send_data_to_api_2(self):
        # Dados para enviar na requisição POST
        # Dados que vamos enviar para a API
        data = {
                "cell_user_info": {
                    "ecgi": {
                        "cell_id":  "2",
                        "plmn" :{
                            "mcc" : "mcc",
                            "mnc" : "mnc"
                        }
                    },
                    "ue_info": {
                        "associate_id": {
                            "type": "2",
                            "value": "constante"
                        },
                        "erab_info": {
                            "erab_id": 14,
                            "erab_qos_parameters": {
                                "qci": 1,
                                "qos_information": {
                                    "erab_gbr_dl": 6,
                                    "erab_gbr_ul": 7,
                                    "erab_mbr_dl": 7,
                                    "erab_mbr_ul": 7
                                }
                            }
                        }
                    }
                },
                "request_id": "1",
                "time_stamp": {
                    "nano_seconds": 9,
                    "seconds": 9
                }
            }
            
        # Enviar a requisição POST para a API
        response = self.client.post("http://127.0.0.1:5000/rni/v2/queries/rab_info/2", json=data)

        # Exibir o status da resposta (opcional)
        print(f"Status da resposta 2: {response.status_code}")
        print(f"Resposta 2: {response.text}")

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
                'coluna1': coluna1,
                'coluna2': coluna2,
                'coluna3': coluna3
                # ...
            }


        # Enviar a requisição POST para a API
        response = self.client.post("http://127.0.0.1:5000/rni/v2/queries/rab_info/3", json=data)

        # Exibir o status da resposta (opcional)
        print(f"Status da resposta 2: {response.status_code}")
        print(f"Resposta 2: {response.text}")

    #Execute o comando locust -f locust_script.py -H http://127.0.0.1:5000 
    #e a interface gráfica deve aparecer no endereço http://127.0.0.1:8089/