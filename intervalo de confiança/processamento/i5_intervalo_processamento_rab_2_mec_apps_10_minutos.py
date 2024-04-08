import numpy as np
from scipy import stats

# Processamento em milissegundos

# 100 #
processamento_interno_100_2 = np.array([4.722, 5.038, 4.837, 5.276, 4.671, 4.978, 4.550, 5.035, 4.910, 4.780])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_100_2 = np.array([6.820, 7.140, 6.975, 7.400, 6.819, 7.110, 6.684, 7.163, 7.029, 6.904])  # 2 mec apps processamento até o cliente 10 minutos

# 200 #
processamento_interno_200_2 = np.array([4.775, 5.723, 5.275, 4.901, 5.277, 5.161, 4.923, 5.228, 5.623, 5.451])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_200_2 = np.array([6.942, 7.830, 7.513, 7.096, 7.481, 7.346, 7.174, 7.428, 7.828, 7.699])  # 2 mec apps processamento até o cliente 10 minutos

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
