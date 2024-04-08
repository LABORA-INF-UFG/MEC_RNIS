import numpy as np
from scipy import stats

# Processamento em milissegundos

# 100 #
processamento_interno_100_4 = np.array([9.898, 9.414, 9.373, 9.080, 9.936, 10.664, 9.191, 10.357, 11.397, 12.817])  # 4 mec apps processamento interno 10 minutos
processamento_cliente_100_4 = np.array([12.686, 12.497, 12.468, 12.112, 12.907, 13.809, 12.332, 13.406, 14.507, 15.751])  # 4 mec apps processamento até o cliente 10 minutos

# 200 #
processamento_interno_200_4 = np.array([11.867, 16.236, 12.722, 13.938, 17.609, 13.159, 17.235, 16.562, 13.377, 13.592])  # 4 mec apps processamento interno 10 minutos
processamento_cliente_200_4 = np.array([14.848, 19.241, 15.679, 16.922, 20.588, 16.158, 20.240, 19.713, 16.449, 16.562])  # 4 mec apps processamento até o cliente 10 minutos

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
intervalo_confianca_interno_100_4 = calcular_intervalo_confianca(processamento_interno_100_4)
intervalo_confianca_cliente_100_4 = calcular_intervalo_confianca(processamento_cliente_100_4)
intervalo_confianca_interno_200_4 = calcular_intervalo_confianca(processamento_interno_200_4)
intervalo_confianca_cliente_200_4 = calcular_intervalo_confianca(processamento_cliente_200_4)

# Imprimir resultados
print("Intervalo de Confiança para 100_2 (95%):", intervalo_confianca_interno_100_4)
print("Intervalo de Confiança para 100_2 (95%):", intervalo_confianca_cliente_100_4)
print("Intervalo de Confiança para 200_2 (95%):", intervalo_confianca_interno_200_4)
print("Intervalo de Confiança para 200_2 (95%):", intervalo_confianca_cliente_200_4)
