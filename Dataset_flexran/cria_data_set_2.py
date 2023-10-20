import csv
import random
from faker import Faker
from decimal import Decimal
import datetime

# Função para serializar objetos Decimal
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

fake = Faker()

# Gere o dataset aleatório
dataset = []

for _ in range(1500):
    data_point = {
        "cell_user_info": {
            "ecgi": {
                "cell_id": fake.random_int(min=1, max=1000),
                "plmn": {
                    "mcc": fake.random_int(min=100, max=999),
                    "mnc": fake.random_int(min=10, max=99),
                }
            },
            "ue_info": {
                "associate_id": {
                    "type": fake.random_int(min=1, max=10),
                    "value": fake.word()
                },
                "erab_info": {
                    "erab_id": fake.random_int(min=1, max=20),
                    "erab_qos_parameters": {
                        "qci": fake.random_int(min=1, max=10),
                        "qos_information": {
                            "erab_gbr_dl": Decimal(random.uniform(1, 100)),
                            "erab_gbr_ul": Decimal(random.uniform(1, 100)),
                            "erab_mbr_dl": Decimal(random.uniform(1, 100)),
                            "erab_mbr_ul": Decimal(random.uniform(1, 100)),
                        }
                    }
                }
            },
        },
        "request_id": fake.random_int(min=1, max=1000),
        "time_stamp": {
            "nano_seconds": fake.random_int(min=1, max=999),
            "seconds": int(datetime.datetime.now().timestamp())
        }
    }
    dataset.append(data_point)

# Defina o cabeçalho do CSV
csv_header = [
    "cell_id", "mcc", "mnc", "associate_id_type", "associate_id_value",
    "erab_id", "qci", "erab_gbr_dl", "erab_gbr_ul", "erab_mbr_dl", "erab_mbr_ul",
    "request_id", "nano_seconds", "seconds"
]

# Salve o dataset em um arquivo CSV
with open("radio_network_data.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_header)
    writer.writeheader()
    
    for data_point in dataset:
        row = {
            "cell_id": data_point["cell_user_info"]["ecgi"]["cell_id"],
            "mcc": data_point["cell_user_info"]["ecgi"]["plmn"]["mcc"],
            "mnc": data_point["cell_user_info"]["ecgi"]["plmn"]["mnc"],
            "associate_id_type": data_point["cell_user_info"]["ue_info"]["associate_id"]["type"],
            "associate_id_value": data_point["cell_user_info"]["ue_info"]["associate_id"]["value"],
            "erab_id": data_point["cell_user_info"]["ue_info"]["erab_info"]["erab_id"],
            "qci": data_point["cell_user_info"]["ue_info"]["erab_info"]["erab_qos_parameters"]["qci"],
            "erab_gbr_dl": data_point["cell_user_info"]["ue_info"]["erab_info"]["erab_qos_parameters"]["qos_information"]["erab_gbr_dl"],
            "erab_gbr_ul": data_point["cell_user_info"]["ue_info"]["erab_info"]["erab_qos_parameters"]["qos_information"]["erab_gbr_ul"],
            "erab_mbr_dl": data_point["cell_user_info"]["ue_info"]["erab_info"]["erab_qos_parameters"]["qos_information"]["erab_mbr_dl"],
            "erab_mbr_ul": data_point["cell_user_info"]["ue_info"]["erab_info"]["erab_qos_parameters"]["qos_information"]["erab_mbr_ul"],
            "request_id": data_point["request_id"],
            "nano_seconds": data_point["time_stamp"]["nano_seconds"],
            "seconds": data_point["time_stamp"]["seconds"]
        }
        writer.writerow(row)

print("Dataset gerado e salvo no formato CSV com sucesso.")
