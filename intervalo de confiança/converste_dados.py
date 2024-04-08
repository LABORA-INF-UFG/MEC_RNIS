import re

numeros = [
    "19.569.418.416.521",
    "19.593.778.682.634",
    "18.494.094.346.046",
    "19.537.276.839.254",
    "19.202.331.667.102",
    "19.006.687.336.039",
    "18.991.998.372.076",
    "19.356.684.111.794",
    "18.749.843.802.110",
    "19.183.606.291.152"
]

# Removendo do segundo ponto em diante
numeros_formatados = [re.sub(r'(\.\d+){3}', '', numero) for numero in numeros]

print(numeros_formatados)
