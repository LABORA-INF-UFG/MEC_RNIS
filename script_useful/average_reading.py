# Nome do arquivo de texto com os valores de tempo
nome_arquivo = 'tempos_decorridos_rab_10.txt'

# Inicialize uma lista para armazenar os valores de tempo
tempos = []

# Abra o arquivo e leia os valores
with open(nome_arquivo, 'r') as arquivo:
    for linha in arquivo:
        tempo = float(linha.strip())  # Converte a linha em um número de ponto flutuante
        tempos.append(tempo)

# Cálculo da média
media_segundos = sum(tempos) / len(tempos)
media_milissegundos = media_segundos * 1000

print(f"Média em Milissegundos: {media_milissegundos:.12f} milissegundos")
