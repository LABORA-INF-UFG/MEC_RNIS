import numpy as np
from scipy import stats

# Processamento em milissegundos

# 100 #
processamento_interno_100_2 = np.array([8.619, 8.583, 7.881, 7.784, 7.905, 8.005, 7.783, 7.736, 7.540, 7.334])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_100_2 = np.array([13.233, 12.701, 12.006, 11.883, 12.001, 12.114, 11.891, 11.846, 11.658, 11.504])  # 2 mec apps processamento até o cliente 10 minutos

# 200 #
processamento_interno_200_2 = np.array([8.989, 8.825, 8.435, 8.130, 8.195, 8.049, 8.449, 8.579, 8.244, 8.202])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_200_2 = np.array([13.588, 13.302, 12.734, 12.519, 12.516, 12.392, 12.775, 12.859, 12.628, 12.559])  # 2 mec apps processamento até o cliente 10 minutos

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
