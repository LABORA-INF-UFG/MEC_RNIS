import matplotlib
matplotlib.use('Agg')  # Define o backend como Agg

import matplotlib.pyplot as plt
from PIL import Image

# Dados do primeiro gráfico
quantidade_requisicoes_atendidas = [23685, 22100.8, 19086.1, 16598.3, 17773.5, 15108.8, 14838.2, 14912.1]
quantidade_informacoes_nao_atendidas = [0, 0, 2337.7, 18306.5, 20822.7, 31336.4, 84836, 82163.8]

# Criando o primeiro gráfico
fig, ax = plt.subplots()
index = range(len(quantidade_informacoes_nao_atendidas))
bar_width = 0.35
ax.bar(index, quantidade_requisicoes_atendidas, bar_width, color='gray', label='Requisições Atendidas')
ax.bar([i + bar_width for i in index], quantidade_informacoes_nao_atendidas, bar_width, color='black', label='Requisições Não Atendidas')

fontsize = 6
for i in index:
    ax.text(i, quantidade_requisicoes_atendidas[i], str(int(quantidade_requisicoes_atendidas[i])), ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    ax.text(i + bar_width, quantidade_informacoes_nao_atendidas[i], str(int(quantidade_informacoes_nao_atendidas[i])), ha='center', va='bottom', fontsize=fontsize, fontweight='bold')

ax.set_xlabel('Usuários enviando informações')
ax.set_ylabel('Requisições')
ax.set_xticks([i + bar_width/2 for i in index])
ax.set_xticklabels([100, 200, 400, 600, 800, 1000, 1500, 2000])
ax.legend()

ax.text(0.5, 1.1, '8 MEC Apps', ha='center', va='center', fontsize=12, transform=ax.transAxes)

# Salva o primeiro gráfico em um arquivo temporário
fig_path = 'temp_fig1.png'
fig.savefig(fig_path)

# Fecha a figura do primeiro gráfico
plt.close(fig)


# Dados do segundo gráfico

quantidade_requisicoes_atendidas_2 = [14391.4, 13480.4, 10556.9, 9346.3, 10048.4, 8317.8, 8215.3, 8424.5]
quantidade_informacoes_nao_atendidas_2 = [0, 0, 401.6, 11552.3, 14090.6, 21316.7, 57855.9, 55053.8]


# Criando o segundo gráfico
fig2, ax2 = plt.subplots()
index = range(len(quantidade_informacoes_nao_atendidas_2))
bar_width = 0.35
ax2.bar(index, quantidade_requisicoes_atendidas_2, bar_width, color='gray', label='Requisições Atendidas')
ax2.bar([i + bar_width for i in index], quantidade_informacoes_nao_atendidas_2, bar_width, color='black', label='Requisições Não Atendidas')

fontsize = 6
for i in index:
    ax2.text(i, quantidade_requisicoes_atendidas_2[i], str(int(quantidade_requisicoes_atendidas_2[i])), ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    ax2.text(i + bar_width, quantidade_informacoes_nao_atendidas_2[i], str(int(quantidade_informacoes_nao_atendidas_2[i])), ha='center', va='bottom', fontsize=fontsize, fontweight='bold')

ax2.set_xlabel('Usuários enviando informações')
ax2.set_ylabel('Requisições')
ax2.set_xticks([i + bar_width/2 for i in index])
ax2.set_xticklabels([100, 200, 400, 600, 800, 1000, 1500, 2000])
ax2.legend()

ax2.text(0.5, 1.1, '8 MEC Apps', ha='center', va='center', fontsize=12, transform=ax.transAxes)

# Salva o segundo gráfico em um arquivo temporário
fig2_path = 'temp_fig2.png'
fig2.savefig(fig2_path)

# Fecha a figura do segundo gráfico
plt.close(fig2)

# Carrega os gráficos como imagens
img1 = Image.open(fig_path)
img2 = Image.open(fig2_path)

# Calcula a largura total da imagem combinada
total_width = img1.width + img2.width

# Calcula a altura total da imagem combinada
max_height = max(img1.height, img2.height)

# Cria uma nova imagem com a largura total e altura máxima das duas imagens
new_img = Image.new('RGB', (total_width, max_height))

# Coloca as imagens lado a lado
new_img.paste(img1, (0, 0))
new_img.paste(img2, (img1.width, 0))

# Salva a imagem combinada
new_img.save('combined_graphs_plmn_8_mec_apps.png')
