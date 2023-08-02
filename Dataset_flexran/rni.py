import csv

# Lista para armazenar as informações da RNI
rni_data = []

# Gerar 100 informações de exemplo da RNI
for i in range(500):
    rni_i ={
        "cell_user_info": {
            "cell_user_info": {
                "ecgi": {
                    "cell_id":  f"{i+1}",
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
            }
        },
        "returnues_id":{
            "request_id": "1",
        },
        "time_stamp": {
            "time_stamp": {
                "nano_seconds": 12,
                "seconds": 13
            }
        }
    }
    rni_data.append(rni_i)

# Caminho do arquivo CSV
csv_path = 'rni.csv'

# Criação do arquivo CSV
with open(csv_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=rni_data[0].keys())

    # Escreve o cabeçalho do arquivo CSV
    writer.writeheader()

    # Escreve as linhas de dados
    writer.writerows(rni_data)

print(f'Arquivo CSV "{csv_path}" criado com sucesso com 100 informações da RNI!')
