# Lista de nomes dos arquivos de texto
nomes_arquivos_plmn_client = ['tempos_decorridos_plmn_client_1.txt', 'tempos_decorridos_plmn_client_2.txt', 'tempos_decorridos_plmn_client_3.txt', 'tempos_decorridos_plmn_client_4.txt', 'tempos_decorridos_plmn_client_5.txt', 'tempos_decorridos_plmn_client_6.txt', 'tempos_decorridos_plmn_client_7.txt', 'tempos_decorridos_plmn_client_8.txt', 'tempos_decorridos_plmn_client_9.txt', 'tempos_decorridos_plmn_client_10.txt']

nomes_arquivos_rab_client = ['tempos_decorridos_rab_client_1.txt', 'tempos_decorridos_rab_client_2.txt', 'tempos_decorridos_rab_client_3.txt', 'tempos_decorridos_rab_client_4.txt', 'tempos_decorridos_rab_client_5.txt', 'tempos_decorridos_rab_client_6.txt', 'tempos_decorridos_rab_client_7.txt', 'tempos_decorridos_rab_client_8.txt', 'tempos_decorridos_rab_client_9.txt', 'tempos_decorridos_rab_client_10.txt']

nomes_arquivos_plmn = ['tempos_decorridos_plmn_1.txt', 'tempos_decorridos_plmn_2.txt', 'tempos_decorridos_plmn_3.txt', 'tempos_decorridos_plmn_4.txt', 'tempos_decorridos_plmn_5.txt', 'tempos_decorridos_plmn_6.txt', 'tempos_decorridos_plmn_7.txt', 'tempos_decorridos_plmn_8.txt', 'tempos_decorridos_plmn_9.txt', 'tempos_decorridos_plmn_10.txt']

nomes_arquivos_rab = ['tempos_decorridos_rab_1.txt', 'tempos_decorridos_rab_2.txt', 'tempos_decorridos_rab_3.txt', 'tempos_decorridos_rab_4.txt', 'tempos_decorridos_rab_5.txt', 'tempos_decorridos_rab_6.txt', 'tempos_decorridos_rab_7.txt', 'tempos_decorridos_rab_8.txt', 'tempos_decorridos_rab_9.txt', 'tempos_decorridos_rab_10.txt']


cliente_plmn_1 = ['tempos_decorridos_plmn_1_client_1.txt', 'tempos_decorridos_plmn_1_client_2.txt', 'tempos_decorridos_plmn_1_client_3.txt', 'tempos_decorridos_plmn_1_client_4.txt', 'tempos_decorridos_plmn_1_client_5.txt', 'tempos_decorridos_plmn_1_client_6.txt', 'tempos_decorridos_plmn_1_client_7.txt', 'tempos_decorridos_plmn_1_client_8.txt', 'tempos_decorridos_plmn_1_client_9.txt', 'tempos_decorridos_plmn_1_client_10.txt']

cliente_plmn_2 = ['tempos_decorridos_plmn_2_client_1.txt', 'tempos_decorridos_plmn_2_client_2.txt', 'tempos_decorridos_plmn_2_client_3.txt', 'tempos_decorridos_plmn_2_client_4.txt', 'tempos_decorridos_plmn_2_client_5.txt', 'tempos_decorridos_plmn_2_client_6.txt', 'tempos_decorridos_plmn_2_client_7.txt', 'tempos_decorridos_plmn_2_client_8.txt', 'tempos_decorridos_plmn_2_client_9.txt', 'tempos_decorridos_plmn_2_client_10.txt']

cliente_rab_3 = ['tempos_decorridos_rab_3_client_1.txt', 'tempos_decorridos_rab_3_client_2.txt', 'tempos_decorridos_rab_3_client_3.txt', 'tempos_decorridos_rab_3_client_4.txt', 'tempos_decorridos_rab_3_client_5.txt', 'tempos_decorridos_rab_3_client_6.txt', 'tempos_decorridos_rab_3_client_7.txt', 'tempos_decorridos_rab_3_client_8.txt', 'tempos_decorridos_rab_3_client_9.txt', 'tempos_decorridos_rab_3_client_10.txt']

cliente_rab_4 = ['tempos_decorridos_rab_4_client_1.txt', 'tempos_decorridos_rab_4_client_2.txt', 'tempos_decorridos_rab_4_client_3.txt', 'tempos_decorridos_rab_4_client_4.txt', 'tempos_decorridos_rab_4_client_5.txt', 'tempos_decorridos_rab_4_client_6.txt', 'tempos_decorridos_rab_4_client_7.txt', 'tempos_decorridos_rab_4_client_8.txt', 'tempos_decorridos_rab_4_client_9.txt', 'tempos_decorridos_rab_4_client_10.txt']

rnis_plmn = ['tempos_decorridos_plmn_1.txt', 'tempos_decorridos_plmn_2.txt', 'tempos_decorridos_plmn_3.txt', 'tempos_decorridos_plmn_4.txt', 'tempos_decorridos_plmn_5.txt', 'tempos_decorridos_plmn_6.txt', 'tempos_decorridos_plmn_7.txt', 'tempos_decorridos_plmn_8.txt', 'tempos_decorridos_plmn_9.txt', 'tempos_decorridos_plmn_10.txt']

rnis_rab = ['tempos_decorridos_rab_1.txt', 'tempos_decorridos_rab_2.txt', 'tempos_decorridos_rab_3.txt', 'tempos_decorridos_rab_4.txt', 'tempos_decorridos_rab_5.txt', 'tempos_decorridos_rab_6.txt', 'tempos_decorridos_rab_7.txt', 'tempos_decorridos_rab_8.txt', 'tempos_decorridos_rab_9.txt', 'tempos_decorridos_rab_10.txt']

# Inicialize uma lista para armazenar as médias de cada arquivo
medias_milissegundos = []

# Processa cada arquivo
for nome_arquivo in nomes_arquivos_rab_client:
    tempos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            tempo = float(linha.strip())  # Converte a linha em um número de ponto flutuante
            tempos.append(tempo)

    # Cálculo da média em milissegundos
    media_segundos = sum(tempos) / len(tempos)
    media_milissegundos = media_segundos * 1000
    medias_milissegundos.append(media_milissegundos)

# Calcula a média das médias
media_total_milissegundos = sum(medias_milissegundos) / len(medias_milissegundos)

# Salva o resultado em um arquivo de texto
with open('media_resultado_rab_client.txt', 'w') as resultado_arquivo:
    for media in medias_milissegundos:
        resultado_arquivo.write(f'Média em Milissegundos: {media:.12f} milissegundos\n')
    resultado_arquivo.write(f'Média Total em Milissegundos: {media_total_milissegundos:.12f} milissegundos\n')

print(f'Médias calculadas e resultado salvo em "media_resultado.txt"')
