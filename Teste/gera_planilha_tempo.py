import os
import pandas as pd

# Caminho onde os arquivos TXT estão localizados
caminho_dos_arquivos = "/home/kaique/Documentos/ufg/MEC_RNIS/Teste/"

# Lista para armazenar os dados
dados = []

# Loop pelos arquivos no diretório
for nome_arquivo in os.listdir(caminho_dos_arquivos):
    if nome_arquivo.endswith(".txt"):
        caminho_completo = os.path.join(caminho_dos_arquivos, nome_arquivo)
        
        # Adiciona uma linha em branco para separar os dados de cada arquivo
        dados.append({'Nome do Arquivo': '', 'Valor': ''})

        # Leitura do conteúdo do arquivo
        with open(caminho_completo, 'r') as arquivo:
            for linha in arquivo:
                # Adiciona os dados à lista
                dados.append({'Nome do Arquivo': nome_arquivo, 'Valor': linha.strip()})

# Cria um DataFrame pandas com os dados
df = pd.DataFrame(dados)

# Salva o DataFrame em um arquivo Excel
caminho_planilha = "/home/kaique/Documentos/ufg/MEC_RNIS/Teste/planilha.xlsx"
df.to_excel(caminho_planilha, index=False)

print(f"Os dados foram salvos em {caminho_planilha}")