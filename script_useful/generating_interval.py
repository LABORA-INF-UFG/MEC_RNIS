import numpy as np
from scipy import stats

# install: pip install scipy

# Lista de tempos de exemplo (substitua pelos seus próprios dados)
tempo = [5.2, 6.1, 4.8, 7.3, 6.0, 5.5, 7.9, 6.4, 5.8]

# Nível de confiança desejado (por exemplo, 95%)
confidence_level = 0.95

# Cálculo da média e desvio padrão da amostra
mean_tempo = np.mean(tempo)
std_tempo = np.std(tempo, ddof=1)  # Use ddof=1 para correção de Bessel

# Tamanho da amostra
sample_size = len(tempo)

# Graus de liberdade (para distribuição t)
degrees_of_freedom = sample_size - 1

# Valor crítico (t para uma distribuição t)
critical_value = stats.t.ppf(1 - (1 - confidence_level) / 2, df=degrees_of_freedom)

# Erro padrão da média
standard_error = std_tempo / np.sqrt(sample_size)

# Intervalo de confiança
margin_of_error = critical_value * standard_error
confidence_interval = (mean_tempo - margin_of_error, mean_tempo + margin_of_error)

print(f"Intervalo de Confiança de {confidence_level * 100}%:")
print(f"Média da Amostra: {mean_tempo}")
print(f"Erro Padrão da Média: {standard_error}")
print(f"Valor Crítico (t): {critical_value}")
print(f"Margem de Erro: {margin_of_error}")
print(f"Intervalo de Confiança: {confidence_interval}")
