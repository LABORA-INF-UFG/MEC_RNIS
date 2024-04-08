import numpy as np
from scipy import stats

# Processamento em milissegundos

# 100 #
processamento_interno_100_2 = np.array([12.812, 12.567, 12.045, 11.839, 11.282, 11.456, 13.050, 12.148, 11.785, 12.498])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_100_2 = np.array([20.473, 19.967, 19.634, 19.467, 18.840, 19.004, 20.123, 19.625, 19.243, 19.862])  # 2 mec apps processamento até o cliente 10 minutos

# 200 #
processamento_interno_200_2 = np.array([13.996, 12.686, 12.751, 12.882, 13.269, 13.247, 12.762, 12.732, 12.547, 13.055])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_200_2 = np.array([22.642, 20.593, 20.664, 20.777, 21.908, 20.984, 20.727, 20.519, 20.505, 20.942])  # 2 mec apps processamento até o cliente 10 minutos

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
