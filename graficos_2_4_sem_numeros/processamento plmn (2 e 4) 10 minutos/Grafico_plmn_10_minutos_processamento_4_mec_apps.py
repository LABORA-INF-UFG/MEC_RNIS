import matplotlib
matplotlib.use('Agg')  # Define o backend como Agg

import matplotlib.pyplot as plt
from PIL import Image

# Dados do primeiro gráfico
processamento_interno = [10.213, 14.630, 8.076, 6.176, 5.662, 6.651, 6.606, 7.024]
processamento_ate_o_cliente = [13.247, 17.640, 11.141, 9.007, 8.320, 9.458, 9.544, 10.168]

# Criando o primeiro gráfico
fig, ax = plt.subplots()
index = range(len(processamento_ate_o_cliente))
bar_width = 0.35
ax.bar(index, processamento_interno, bar_width, color='blue', label='Processamento interno')
ax.bar([i + bar_width for i in index], processamento_ate_o_cliente, bar_width, color='red', label='Processamento até o cliente')

# fontsize = 6
# for i in index:
#     ax.text(i, processamento_interno[i], f"{processamento_interno[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     ax.text(i + bar_width, processamento_ate_o_cliente[i], f"{processamento_ate_o_cliente[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')

ax.set_xlabel('Usuários enviando informações')
ax.set_ylabel('Milissegundos')
ax.set_xticks([i + bar_width/2 for i in index])
ax.set_xticklabels([100, 200, 400, 600, 800, 1000, 1500, 2000])
ax.legend()

ax.text(0.5, 1.1, '4 MEC Apps', ha='center', va='center', fontsize=12, transform=ax.transAxes)

# Salva o primeiro gráfico em um arquivo temporário
fig_path = 'temp_fig1.png'
fig.savefig(fig_path)

# Fecha a figura do primeiro gráfico
plt.close(fig)

# Dados do segundo gráfico
processamento_interno_2 = [15.221, 16.509, 18.736, 11.614, 11.248, 12.136, 13.246, 13.711]
processamento_ate_o_cliente_2 = [21.790, 23.776, 26.291, 17.846, 16.922, 18.130, 19.475, 20.114]

# Criando o segundo gráfico
fig2, ax2 = plt.subplots()
index = range(len(processamento_ate_o_cliente_2))
bar_width = 0.35
ax2.bar(index, processamento_interno_2, bar_width, color='blue', label='Processamento interno')
ax2.bar([i + bar_width for i in index], processamento_ate_o_cliente_2, bar_width, color='red', label='Processamento até o cliente')

# fontsize = 6
# for i in index:
#     ax2.text(i, processamento_interno_2[i], f"{processamento_interno_2[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     ax2.text(i + bar_width, processamento_ate_o_cliente_2[i], f"{processamento_ate_o_cliente_2[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')

ax2.set_xlabel('Usuários enviando informações')
ax2.set_ylabel('Milissegundos')
ax2.set_xticks([i + bar_width/2 for i in index])
ax2.set_xticklabels([100, 200, 400, 600, 800, 1000, 1500, 2000])
ax2.legend()

ax2.text(0.5, 1.1, '4 MEC Apps', ha='center', va='center', fontsize=12, transform=ax.transAxes)

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
new_img.save('combined_graphs_plmn_4_mec_apps.png')
