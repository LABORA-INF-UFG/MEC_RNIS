import numpy as np
from scipy import stats

# Conjunto de dados 1
dados1 = np.array([32126, 38967, 36793, 37407, 38923, 35648, 37999, 37202, 33083, 31510])

# Conjunto de dados 2
dados2 = np.array([15171, 12914, 15037, 14549, 12893, 16778, 13952, 15139, 19332, 21002])

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
