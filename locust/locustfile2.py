from locust import HttpUser, task, between
import pandas as pd

# Criaremos a classe ApiUser, que herda da classe HttpUser e nos dá a possibilidade de realizar requests do tipo HTTP. 
class ApiUser(HttpUser):
    
    #inserimos a informação do intervalo de tempo entre 1 e 3 segundos entre as requests enviadas.
    wait_time = between(1, 3)

    # especificamos nossas tasks para os testes através do decorator @task 
    @task
    def send_data_rab(self):
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
        #print(f"Resposta 1: {response.text}")

    # especificamos nossas tasks para os testes através do decorator @task 
    @task
    def send_data_plmn(self):
        # Dados para enviar na requisição POST
        # Dados que vamos enviar para a API
        data = {
                "plmn" : {
                    "mcc" : "mcc",
                    "mnc" : "mnc"
                },
                "time_stamp" : {
                    "nano_seconds" : 12,
                    "seconds": 13
                }
            }
            
        # Enviar a requisição POST para a API
        response = self.client.post("http://127.0.0.1:5000/rni/v2/queries/plmn_info/1", json=data)

        # Exibir o status da resposta (opcional)
        print(f"Status da resposta 1: {response.status_code}")
        #print(f"Resposta 1: {response.text}")



    #Execute o comando locust -f locust_script.py -H http://127.0.0.1:5000 
    #e a interface gráfica deve aparecer no endereço http://127.0.0.1:8089/