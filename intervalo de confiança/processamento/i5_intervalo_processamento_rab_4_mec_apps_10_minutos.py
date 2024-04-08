import numpy as np
from scipy import stats

# Processamento em milissegundos

# 100 #
processamento_interno_100_4 = np.array([6.297, 7.023, 6.992, 6.696, 6.359, 8.027, 7.627, 7.408, 8.986, 8.016])  # 4 mec apps processamento interno 10 minutos
processamento_cliente_100_4 = np.array([9.554, 10.469, 10.416, 10.125, 9.884, 11.448, 11.029, 10.867, 12.360, 11.591])  # 4 mec apps processamento até o cliente 10 minutos

# 200 #
processamento_interno_200_4 = np.array([24.707, 22.978, 22.983, 23.726, 23.763, 7.808, 10.094, 9.599, 8.277, 10.080])  # 4 mec apps processamento interno 10 minutos
processamento_cliente_200_4 = np.array([11.994, 12.492, 11.443, 11.830, 13.992, 11.247, 13.382, 13.103, 11.728, 13.428])  # 4 mec apps processamento até o cliente 10 minutos

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
