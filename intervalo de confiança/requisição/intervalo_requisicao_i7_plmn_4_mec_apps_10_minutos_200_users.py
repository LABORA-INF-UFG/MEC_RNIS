import numpy as np
from scipy import stats

# Conjunto de dados 1
dados1 = np.array([63668, 53653, 55046, 55057, 60966, 51722, 49039, 54736, 49936, 58138])

# Conjunto de dados 2
dados2 = np.array([24686, 28933, 28478, 28487, 22507, 31793, 34177, 28273, 33518, 24973])

# Função para calcular o intervalo de confiança
def intervalo_confianca(dados):
    media = np.mean(dados)
    desvio_padrao = np.std(dados, ddof=1)
    tamanho_amostra = len(dados)
    erro_padrao = desvio_padrao / np.sqrt(tamanho_amostra)
    intervalo = erro_padrao * stats.t.ppf((1 + 0.95) / 2, tamanho_amostra - 1)
    limite_inferior = media - intervalo
    limite_superior = media + intervalo
    return (limite_inferior, limite_superior)

# Calculando o intervalo de confiança para os conjuntos de dados
ic_dados1 = intervalo_confianca(dados1)
ic_dados2 = intervalo_confianca(dados2)

print("Intervalo de Confiança de 95% para o primeiro conjunto de dados:", ic_dados1)
print("Intervalo de Confiança de 95% para o segundo conjunto de dados:", ic_dados2)
