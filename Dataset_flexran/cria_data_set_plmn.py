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

# Gere o dataset aleatório no novo formato
dataset = []

for _ in range(15000):
    data_point = {
        "plmn": {
            "mcc": str(random.randint(1000, 9999)),
            "mnc": str(random.randint(100, 999))
        },
        "time_stamp": {
            "nano_seconds": random.randint(1, 999999999),
            "seconds": int(datetime.datetime.now().timestamp())
        }
    }
    dataset.append(data_point)

# Salve o dataset em um arquivo JSON
with open("novo_dataset_plmn.json", "w") as file:
    json.dump(dataset, file, indent=4, default=decimal_default)

print("Novo dataset gerado e salvo com sucesso.")
