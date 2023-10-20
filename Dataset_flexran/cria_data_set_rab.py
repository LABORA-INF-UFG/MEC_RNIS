import json
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

for _ in range(15000):
    data_point = {
        "cell_user_info": {
            "ecgi": {
                "cell_id": fake.random_int(min=1, max=100000),
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
                            "erab_gbr_dl": Decimal(random.uniform(1, 1000)),
                            "erab_gbr_ul": Decimal(random.uniform(1, 1000)),
                            "erab_mbr_dl": Decimal(random.uniform(1, 1000)),
                            "erab_mbr_ul": Decimal(random.uniform(1, 1000)),
                        }
                    }
                }
            },
        },
        "request_id": fake.random_int(min=1, max=10000),
        "time_stamp": {
            "nano_seconds": fake.random_int(min=1, max=9999),
            "seconds": int(datetime.datetime.now().timestamp())
        }
    }
    dataset.append(data_point)

# Salve o dataset em um arquivo JSON
with open("radio_network_data.json", "w") as file:
    json.dump(dataset, file, indent=4, default=decimal_default)

print("Dataset gerado e salvo com sucesso.")
