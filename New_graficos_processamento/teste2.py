import matplotlib
matplotlib.use('Agg')  # Define o backend como Agg

import matplotlib.pyplot as plt

# Dados do primeiro gráfico 2 Mec App
processamento_interno = [6.098, 7.184, 5.961, 4.540, 4.009, 4.385, 4.567, 4.629]
processamento_ate_o_cliente = [8.1479, 9.234, 8.155, 6.506, 5.863, 6.295, 6.598, 6.730]

# Dados do segundo gráfico 4 Mec App
processamento_interno_2 = [10.435, 14.456, 8.137, 6.197, 5.708, 10.788, 6.606, 6.608]
processamento_ate_o_cliente_2 = [13.462, 17.559, 11.201, 9.026, 8.400, 14.674, 9.544, 9.526]

# Dados do terceiro gráfico 6 Mec App
processamento_interno_3 = [20.555, 26.187, 14.504, 20.860, 9.513, 10.768, 11.805, 11.087]
processamento_ate_o_cliente_3 = [24.817, 30.603, 18.867, 26.026, 13.280, 14.618, 15.993, 15.246]

# Dados do quarto gráfico 8 Mec App
processamento_interno_4 = [692.772, 251.431, 43.798, 21.033, 20.052, 38.487, 38.782, 37.606]
processamento_ate_o_cliente_4 = [695.162, 271.027, 49.580, 26.166, 24.840, 43.923, 44.859, 42.937]

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
fontsize = 6
for i in index:
    if processamento_interno[i] <= 24:
        ax.text(i - bar_gap / 2, processamento_interno[i], f"{processamento_interno[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    if processamento_ate_o_cliente[i] <= 24:
        ax.text(i - bar_gap / 2, processamento_ate_o_cliente[i], f"{processamento_ate_o_cliente[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    if processamento_interno_2[i] <= 24:
        ax.text(i + len(processamento_ate_o_cliente) + bar_gap / 2, processamento_interno_2[i], f"{processamento_interno_2[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    if processamento_ate_o_cliente_2[i] <= 24:
        ax.text(i + len(processamento_ate_o_cliente) + bar_gap / 2, processamento_ate_o_cliente_2[i], f"{processamento_ate_o_cliente_2[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    if processamento_interno_3[i] <= 24:
        ax.text(i + 2 * len(processamento_ate_o_cliente) + bar_gap, processamento_interno_3[i], f"{processamento_interno_3[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    if processamento_ate_o_cliente_3[i] <= 24:
        ax.text(i + 2 * len(processamento_ate_o_cliente) + bar_gap, processamento_ate_o_cliente_3[i], f"{processamento_ate_o_cliente_3[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    if processamento_interno_4[i] <= 24:
        ax.text(i + 3 * len(processamento_ate_o_cliente) + bar_gap, processamento_interno_4[i], f"{processamento_interno_4[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')
    if processamento_ate_o_cliente_4[i] <= 24:
        ax.text(i + 3 * len(processamento_ate_o_cliente) + bar_gap, processamento_ate_o_cliente_4[i], f"{processamento_ate_o_cliente_4[i]:.3f}", ha='center', va='bottom', fontsize=fontsize, fontweight='bold')

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
plt.savefig('testeeeee.png')
