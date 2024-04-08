# Intervalo de confiança da quantidade de requisição
# pip install numpy


import numpy as np
from scipy import stats

# processamento em milissegundos
processamento = [4.880, 5.234, 5.124, 4.016, 3.578, 3.782, 4.177, 4.293] # 2 mec apps processamento interno 10 minutos
#processamento = [7.004, 7.434, 7.424, 6.142, 5.553, 5.820, 6.395, 6.536] # 2 mec apps processamento até o cliente 10 minutos

#processamento = [7.343, 9.080, 6.716, 5.274, 4.783, 5.335, 5.595, 5.933] # 4 mec apps processamento interno 10 minutos
#processamento = [10.774, 12.464, 10.034, 8.386, 7.718, 8.423, 8.820, 9.432] # 4 mec apps processamento até o cliente 10 minutos



#processamento = [4.848, 5.164, 5.038, 3.966, 3.577, 3.746, 3.974, 4.058] # 2 mec apps processamento interno 05 minutos
#processamento = [7.014, 7.334, 7.314, 6.024, 5.522, 5.758, 6.117, 6.264] # 2 mec apps processamento interno 05 minutos

#processamento = [7.392, 9.493, 6.688, 5.269, 4.812, 8.036, 5.595, 5.617] # 4 mec apps processamento interno 05 minutos
#processamento = [10.787, 12.877, 10.004, 8.372, 7.764, 12.597, 8.820, 8.833] # 4 mec apps processamento interno 05 minutos


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
