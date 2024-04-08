# Intervalo de confiança da quantidade de requisição
# pip install numpy



import numpy as np
from scipy import stats

# requisicoes PLMN 10 minutos
requisicoes = [60734.7, 57340.4, 47067.4, 41159, 42209.6, 33403.5, 33017.8, 34202.5] # 2 mec apps requisições atendidas 10 minutos
#requisicoes = [0, 0, 6208.9, 37988.7, 49900.6, 82345.7, 196239, 188454.9] # 2 mec apps requisições não atendidas 10 minutos

#requisicoes = [55196.1, 52291.6, 44890.3, 39083, 41193, 32378, 33255.1, 31914] # 4 mec apps requisições atendidas 10 minutos
#requisicoes = [0, 0, 6045.3, 38758.9, 49092.9, 77580.7, 194050.2, 179653.8] # 4 mec apps requisições não atendidas 10 minutos


#requisicoes = [29183.9, 29373.8, 23736.1, 20770.9, 21275.6, 17151.8, 16836.1, 17119.8] # 2 mec apps requisições atendidas 05 minutos
#requisicoes = [0, 0, 3857.1, 19273.8, 26092.4, 40809.7, 101884.9, 96668.8]  # 2 mec apps requisições não atendidas 05 minutos

#requisicoes = [27469.4, 25325.8, 22600.2, 19100.3, 19988.6, 15683.8, 16669.7, 17228] # 4 mec apps requisições atendidas 05 minutos
#requisicoes = [0, 0, 2745.5, 20239.3, 23819.4,36254.7, 97242.5, 95019] # 4 mec apps requisições não atendidas 05 minutos


# Média dos requisicoes
media = np.mean(requisicoes)

# Desvio padrão dos requisicoes
desvio_padrao = np.std(requisicoes, ddof=1)

# Tamanho da amostra
n = len(requisicoes)

# Valor crítico para um nível de confiança de 95%
valor_critico = stats.t.ppf(0.975, df=n-1)

# Margem de erro
margem_erro = valor_critico * (desvio_padrao / np.sqrt(n))

# Intervalo de confiança
intervalo_confianca = (media - margem_erro, media + margem_erro)

print("Intervalo de Confiança (95%):", intervalo_confianca)
