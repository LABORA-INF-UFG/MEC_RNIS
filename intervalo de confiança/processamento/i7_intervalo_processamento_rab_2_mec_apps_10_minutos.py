import numpy as np
from scipy import stats

# Processamento em milissegundos

# 100 #
processamento_interno_100_2 = np.array([12.067, 12.206, 10.832, 12.312, 11.693, 11.479, 11.547, 11.829, 11.441, 11.746])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_100_2 = np.array([19.625, 19.567, 18.612, 19.498, 19.101, 19.028, 19.042, 19.202, 18.820, 19.323])  # 2 mec apps processamento até o cliente 10 minutos

# 200 #
processamento_interno_200_2 = np.array([13.242, 13.297, 13.932, 12.648, 12.178, 12.503, 12.163, 13.156, 12.271, 13.331])  # 2 mec apps processamento interno 10 minutos
processamento_cliente_200_2 = np.array([22.174, 21.271, 21.689, 20.676, 20.155, 20.541, 20.271, 21.122, 20.370, 21.230])  # 2 mec apps processamento até o cliente 10 minutos

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
