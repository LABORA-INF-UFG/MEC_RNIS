import numpy as np
from scipy import stats

# Conjunto de dados 1
dados1 = np.array([31033, 33476, 32952, 28561, 30617, 28282, 32040, 33868, 30291, 29011])

# Conjunto de dados 2
dados2 = np.array([14037, 12643, 14454, 19446, 17249, 19756, 15717, 13775, 17855, 19167])

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
