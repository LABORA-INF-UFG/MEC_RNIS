# Intervalo de confiança da quantidade de requisição
# pip install numpy



import numpy as np
from scipy import stats

# processamento em milissegundos
#processamento = [6.348, 7.153, 5.982, 4.590, 4.039, 4.467, 4.781, 4.993] # 2 mec apps processamento interno 10 minutos
#processamento = [8.353, 9.237, 8.205, 6.616, 5.930, 6.405, 6.896, 7.132] # 2 mec apps processamento até o cliente 10 minutos

#processamento = [10.213, 14.630, 8.076, 6.176, 5.662, 6.651, 6.606, 7.024] # 4 mec apps processamento interno 10 minutos
processamento = [12.735, 12.815, 12.717, 12.852, 12.907, 12.847, 12.948, 12.873, 13.036, 12.627] # 4 mec apps processamento até o cliente 10 minutos



#processamento = [6.098, 7.184, 5.961, 4.540, 4.009, 4.385, 4.567, 4.629] # 2 mec apps processamento interno 05 minutos
#processamento = [8.1479, 9.234, 8.155, 6.506, 5.863, 6.295, 6.598, 6.730] # 2 mec apps processamento interno 05 minutos

#processamento = [10.435, 14.456, 8.137, 6.197, 5.708, 10.788, 6.606, 6.608] # 4 mec apps processamento interno 05 minutos
#processamento = [13.462, 17.559, 11.201, 9.026, 8.400, 14.674, 9.544, 9.526 ] # 4 mec apps processamento interno 05 minutos


# Média dos processamento
media = np.mean(processamento)

# Desvio padrão dos processamento
desvio_padrao = np.std(processamento, ddof=1)

# Tamanho da amostra
n = len(processamento)

# Valor crítico para um nível de confiança de 95%
valor_critico = stats.t.ppf(0.975, df=n-1)

# Margem de erro
margem_erro = valor_critico * (desvio_padrao / np.sqrt(n))

# Intervalo de confiança
intervalo_confianca = (media - margem_erro, media + margem_erro)

print("Intervalo de Confiança (95%):", intervalo_confianca)
