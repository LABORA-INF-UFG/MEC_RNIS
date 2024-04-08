import numpy as np
from scipy import stats

# Processamento em milissegundos

# 100 #
processamento_interno_100_2 = np.array([15.566, 15.058, 15.272, 15.667, 15.701, 15.296, 13.960, 15.591, 15.186, 14.913]) # 2 mec apps processamento interno 10 minutos
processamento_cliente_100_2 = np.array([22.388, 21.739, 21.846, 22.203, 22.008, 21.632, 20.738, 22.074, 21.693, 21.582])  # 2 mec apps processamento até o cliente 10 minutos

# 200 #
processamento_interno_200_2 = np.array([17.976, 16.600, 16.377, 16.518, 17.696, 15.784, 17.926, 16.072, 16.265, 16.966])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_200_2 = np.array([25.377, 23.405, 23.199, 23.437, 24.931, 22.735, 24.672, 22.939, 23.055, 24.010])  # 2 mec apps processamento até o cliente 10 minutos

# Calcular intervalo de confiança para cada grupo
def calcular_intervalo_confianca(processamento):
    # Média dos processamentos
    media = np.mean(processamento)
    
    # Desvio padrão dos processamentos
    desvio_padrao = np.std(processamento, ddof=1)
    
    # Tamanho da amostra
    n = len(processamento)
    
    # Valor crítico para um nível de confiança de 95%
    valor_critico = stats.t.ppf(0.975, df=n-1)
    
    # Margem de erro
    margem_erro = valor_critico * (desvio_padrao / np.sqrt(n))
    
    # Intervalo de confiança
    intervalo_confianca = (media - margem_erro, media + margem_erro)
    
    return intervalo_confianca

# Calcular intervalo de confiança para cada grupo
intervalo_confianca_interno_100_2 = calcular_intervalo_confianca(processamento_interno_100_2)
intervalo_confianca_cliente_100_2 = calcular_intervalo_confianca(processamento_cliente_100_2)
intervalo_confianca_interno_200_2 = calcular_intervalo_confianca(processamento_interno_200_2)
intervalo_confianca_cliente_200_2 = calcular_intervalo_confianca(processamento_cliente_200_2)

# Imprimir resultados
print("Intervalo de Confiança para 100_2 (95%):", intervalo_confianca_interno_100_2)
print("Intervalo de Confiança para 100_2 (95%):", intervalo_confianca_cliente_100_2)
print("Intervalo de Confiança para 200_2 (95%):", intervalo_confianca_interno_200_2)
print("Intervalo de Confiança para 200_2 (95%):", intervalo_confianca_cliente_200_2)
