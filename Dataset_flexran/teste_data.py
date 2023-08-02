import pandas as pd

# Exemplo de JSON
json_data = {
    "nome": "João",
    "idade": 30,
    "email": "joao@example.com",
    "telefone": "(11) 1111-1111"
}

# Converter o JSON para um DataFrame do pandas
df = pd.DataFrame.from_dict([json_data])

# Salvar o DataFrame em um arquivo CSV
df.to_csv('meu_arquivo.csv', index=False)