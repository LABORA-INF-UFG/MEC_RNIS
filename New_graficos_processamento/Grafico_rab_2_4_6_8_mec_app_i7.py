import matplotlib
matplotlib.use('Agg')  # Define o backend como Agg

import matplotlib.pyplot as plt

# Dados do primeiro gráfico 2 Mec App
processamento_interno = [6.590, 7.257, 8.442, 6.495, 5.874, 6.413, 7.028, 7.071]
processamento_ate_o_cliente = [10.934, 11.881, 13.399, 10.720, 9.703, 10.492, 11.382, 11.493]

# Dados do segundo gráfico 4 Mec App
processamento_interno_2 = [11.715, 12.872, 15.037, 9.757, 9.069, 10.211, 10.890, 11.324]
processamento_ate_o_cliente_2 = [19.182, 20.950, 23.800, 16.611, 15.322, 16.977, 17.987, 18.590]

# Dados do terceiro gráfico 6 Mec App
processamento_interno_3 = [35.421, 36.098, 34.505, 17.676, 17.492, 20.160, 20.995, 21.842]
processamento_ate_o_cliente_3 = [48.110, 49.287, 48.661, 28.253, 27.116, 30.812, 32.373, 33.319]

# Dados do quarto gráfico 8 Mec App
processamento_interno_4 = [4767.085, 135.221, 217.464, 42.626, 42.711, 48.163, 48.183, 52.391]
processamento_ate_o_cliente_4 = [4774.152, 155.611, 249.135, 57.386, 56.486, 63.518, 64.209, 68.983]

# Criando o gráfico combinado
fig, ax = plt.subplots(figsize=(10, 6))  # Ajusta o tamanho da figura
index = range(len(processamento_ate_o_cliente))
bar_width = 0.5  # Ajuste o valor para tornar as barras mais grossas
bar_gap = 0.01  # Reduzindo o espaçamento entre os grupos de barras

# Adiciona linhas tracejadas entre os grupos
for i in range(1, 4):
    ax.axvline(i * len(processamento_ate_o_cliente) - 0.5, color='gray', linestyle='--')

# Definindo os rótulos do eixo x
xticks = [100, 200, 400, 600, 800, 1000, 1500, 2000]
xticks_combined = xticks + [x for x in xticks] + [x for x in xticks] + [x for x in xticks]

# Plota os dados do primeiro gráfico
for i in index:
    max_value = max(processamento_interno[i], processamento_ate_o_cliente[i])
    min_value = min(processamento_interno[i], processamento_ate_o_cliente[i])
    ax.bar(i - bar_gap / 2, min_value, bar_width, color='darkblue', edgecolor='white', label='RNIS service processing time (2 MEC Apps)' if i == 0 else '')
    ax.bar(i - bar_gap / 2, max_value - min_value, bar_width, bottom=min_value, color='blue', label='Time to reach MEC App (2 MEC Apps)' if i == 0 else '')

# Plota os dados do segundo gráfico
for i in index:
    max_value2 = max(processamento_interno_2[i], processamento_ate_o_cliente_2[i])
    min_value2 = min(processamento_interno_2[i], processamento_ate_o_cliente_2[i])
    ax.bar(i + len(processamento_ate_o_cliente) + bar_gap / 2, min_value2, bar_width, color='darkgreen', edgecolor='white', label='RNIS service processing time (4 MEC Apps)' if i == 0 else '')
    ax.bar(i + len(processamento_ate_o_cliente) + bar_gap / 2, max_value2 - min_value2, bar_width, bottom=min_value2, color='green', label='Time to reach MEC App (4 MEC Apps)' if i == 0 else '')

# Plota os dados do terceiro gráfico
for i in index:
    max_value3 = max(processamento_interno_3[i], processamento_ate_o_cliente_3[i])
    min_value3 = min(processamento_interno_3[i], processamento_ate_o_cliente_3[i])
    ax.bar(i + 2 * len(processamento_ate_o_cliente) + bar_gap, min_value3, bar_width, color='darkred', edgecolor='white', label='RNIS service processing time (6 MEC Apps)' if i == 0 else '')
    ax.bar(i + 2 * len(processamento_ate_o_cliente) + bar_gap, max_value3 - min_value3, bar_width, bottom=min_value3, color='red', label='Time to reach MEC App (6 MEC Apps)' if i == 0 else '')

# Plota os dados do quarto gráfico
for i in index:
    max_value4 = max(processamento_interno_4[i], processamento_ate_o_cliente_4[i])
    min_value4 = min(processamento_interno_4[i], processamento_ate_o_cliente_4[i])
    ax.bar(i + 3 * len(processamento_ate_o_cliente) + bar_gap, min_value4, bar_width, color='darkorange', edgecolor='white', label='RNIS service processing time (8 MEC Apps)' if i == 0 else '')
    ax.bar(i + 3 * len(processamento_ate_o_cliente) + bar_gap, max_value4 - min_value4, bar_width, bottom=min_value4, color='orange', label='Time to reach MEC App (8 MEC Apps)' if i == 0 else '')

# Limitando o eixo y até 200
plt.ylim(0, 25)

# # Adiciona os valores nos topos das barras
# fontsize = 6
# for i in index:
#     if processamento_interno[i] <= 24:
#         ax.text(i - bar_gap / 2, processamento_interno[i], f"{processamento_interno[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     if processamento_ate_o_cliente[i] <= 24:
#         ax.text(i - bar_gap / 2, processamento_ate_o_cliente[i], f"{processamento_ate_o_cliente[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     if processamento_interno_2[i] <= 24:
#         ax.text(i + len(processamento_ate_o_cliente) + bar_gap / 2, processamento_interno_2[i], f"{processamento_interno_2[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     if processamento_ate_o_cliente_2[i] <= 24:
#         ax.text(i + len(processamento_ate_o_cliente) + bar_gap / 2, processamento_ate_o_cliente_2[i], f"{processamento_ate_o_cliente_2[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     if processamento_interno_3[i] <= 24:
#         ax.text(i + 2 * len(processamento_ate_o_cliente) + bar_gap, processamento_interno_3[i], f"{processamento_interno_3[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     if processamento_ate_o_cliente_3[i] <= 24:
#         ax.text(i + 2 * len(processamento_ate_o_cliente) + bar_gap, processamento_ate_o_cliente_3[i], f"{processamento_ate_o_cliente_3[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     if processamento_interno_4[i] <= 24:
#         ax.text(i + 3 * len(processamento_ate_o_cliente) + bar_gap, processamento_interno_4[i], f"{processamento_interno_4[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
#     if processamento_ate_o_cliente_4[i] <= 24:
#         ax.text(i + 3 * len(processamento_ate_o_cliente) + bar_gap, processamento_ate_o_cliente_4[i], f"{processamento_ate_o_cliente_4[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')

ax.set_xlabel('Number of users')
ax.set_ylabel('Milliseconds')
ax.set_title('Average processing time for requests')
ax.set_xticks(range(len(xticks_combined)))
ax.set_xticklabels(xticks_combined)
ax.tick_params(axis='x', rotation=90)  # Rotaciona os rótulos do eixo x
ax.legend(bbox_to_anchor=(0.5, -0.2), loc='upper center', ncol=2)  # Ajusta a posição da legenda

ax.text(0.10, 1.1, 'i7-10510U', ha='center', va='center', fontsize=12, transform=ax.transAxes)

# Salva o gráfico combinado em um arquivo
plt.tight_layout()  # Ajusta automaticamente
plt.savefig('graphs_proces_rab_combined_i7.png')
