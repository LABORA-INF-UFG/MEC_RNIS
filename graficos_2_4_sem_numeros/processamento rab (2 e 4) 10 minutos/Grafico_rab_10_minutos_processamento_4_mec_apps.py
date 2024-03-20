import matplotlib
matplotlib.use('Agg')  # Define o backend como Agg

import matplotlib.pyplot as plt
from PIL import Image

# Dados do primeiro gráfico
processamento_interno = [7.343, 9.080, 6.716, 5.274, 4.783, 5.335, 5.595, 5.933]
processamento_ate_o_cliente = [10.774, 12.464, 10.034, 8.386, 7.718, 8.423, 8.820, 9.432]

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
processamento_interno_2 = [12.148, 12.993, 14.618, 9.658, 9.318, 10.103, 10.842, 11.201]
processamento_ate_o_cliente_2 = [19.624, 21.026, 23.327, 16.703, 15.692, 16.868, 17.947, 18.499]

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
new_img.save('combined_graphs_rab_4_mec_apps.png')
