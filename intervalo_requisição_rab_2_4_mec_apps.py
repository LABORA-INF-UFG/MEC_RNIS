# Intervalo de confiança da quantidade de requisição
# pip install numpy



import numpy as np
from scipy import stats

# requisicoes PLMN 10 minutos
requisicoes = [31108.5, 27908.7, 24884.3, 20016.4, 21461.7, 17039.9, 17041.6, 17539.4] # 2 mec apps requisições atendidas 10 minutos
#requisicoes = [0,0, 3192, 18423, 25430.3, 41990, 101472.4, 97000.7] # 2 mec apps requisições não atendidas 10 minutos

#requisicoes = [28582.5, 27091.5, 24102, 19310, 19800.7, 16176.5, 16337.1, 15855.7] # 4 mec apps requisições atendidas 10 minutos
#requisicoes = [0, 0, 3274.1, 19168, 23643.5, 38709.9, 95541.5, 89059.6] # 4 mec apps requisições não atendidas 10 minutos


#requisicoes = [15639.1, 13712.8, 12528.1, 10647.1, 10623.7, 8608.9, 8568.2, 8659.5] # 2 mec apps requisições atendidas 05 minutos
#requisicoes = [0, 0, 2042, 9944.3, 13191.4, 20600, 51789.1, 49037.5]  # 2 mec apps requisições não atendidas 05 minutos

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
