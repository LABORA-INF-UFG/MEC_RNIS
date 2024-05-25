import matplotlib
matplotlib.use('Agg')  # Define o backend como Agg

import matplotlib.pyplot as plt

# Dados do primeiro gráfico 2 Mec App
processamento_interno = [4.848, 5.164, 5.038, 3.966, 3.577, 3.746, 3.974, 4.058]
processamento_ate_o_cliente = [7.014, 7.334, 7.314, 6.024, 5.522, 5.758, 6.117, 6.264]

# Dados do segundo gráfico 4 Mec App
processamento_interno_2 = [7.392, 9.493, 6.688, 5.269, 4.812, 8.036, 5.595, 5.617]
processamento_ate_o_cliente_2 = [10.787, 12.877, 10.004, 8.372, 7.764, 12.597, 8.820, 8.833]

# Dados do terceiro gráfico 6 Mec App
processamento_interno_3 = [12.373, 14.108, 10.560, 12.749, 7.546, 8.256, 8.857, 8.675]
processamento_ate_o_cliente_3 = [17.634, 19.365, 15.627, 18.960, 11.950, 12.799, 13.798, 13.556]

# Dados do quarto gráfico 8 Mec App
processamento_interno_4 = [24.965, 30.036, 20.669, 12.941, 12.064, 15.227, 16.184, 16.777]
processamento_ate_o_cliente_4 = [32.848, 37.776, 28.037, 19.345, 18.082, 21.910, 23.314, 23.956]

# Criando o gráfico combinado
fig, ax = plt.subplots(figsize=(10, 6))  # Ajusta o tamanho da figura
index = range(len(processamento_ate_o_cliente))
bar_width = 0.5  # Ajuste o valor para tornar as barras mais grossas
bar_gap = 0.01  # Reduzindo o espaçamento entre os grupos de barras

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

# Adiciona linhas tracejadas entre os grupos
for i in range(1, 4):
    ax.axvline(x=len(processamento_ate_o_cliente) * i - 0.5, linestyle='--', color='gray')

# Limitando o eixo y até 200
plt.ylim(0, 25)

# Adiciona os valores nos topos das barras
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

ax.text(0.10, 1.1, 'i5-10300H', ha='center', va='center', fontsize=12, transform=ax.transAxes)

# Salva o gráfico combinado em um arquivo
plt.tight_layout()  # Ajusta automaticamente
plt.savefig('graphs_proces_rab_combined_i5.png')
