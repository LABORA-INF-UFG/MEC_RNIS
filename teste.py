import numpy as np
from scipy import stats

# Tempos em milissegundos
tempos = [4.848, 5.164, 5.038, 3.966, 3.577, 3.746, 3.974, 4.058]

# Média dos tempos
media = np.mean(tempos)

# Desvio padrão dos tempos
desvio_padrao = np.std(tempos, ddof=1)

# Tamanho da amostra
n = len(tempos)

# Valor crítico para um nível de confiança de 95%
valor_critico = stats.t.ppf(0.975, df=n-1)

# Margem de erro
margem_erro = valor_critico * (desvio_padrao / np.sqrt(n))

# Intervalo de confiança
intervalo_confianca = (media - margem_erro, media + margem_erro)

print("Intervalo de Confiança (95%):", intervalo_confianca)
