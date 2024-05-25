import os
import matplotlib.pyplot as plt
import numpy as np

# Data
requests_served_1 = [15639.1, 13712.8, 12528.1, 10647.1, 10623.7, 8608.9, 8568.2, 8659.5]
requests_not_served_1 = [0, 0, 2042, 9944.3, 13191.4, 20600, 51789.1, 49037.5]

requests_served_2 = [27469.4, 25325.8, 22600.2, 19100.3, 19988.6, 15683.8, 16669.7, 17228]
requests_not_served_2 = [0, 0, 2745.5, 20239.3, 23819.4,36254.7, 97242.5, 95019]

requests_served_3 = [12641.4, 11841.4, 10247.9, 8694.6, 9269.5, 7844.9, 7603.2, 7997.4]
requests_not_served_3 = [0, 0, 1405.2, 9459.2, 11019.7, 18216.1, 44730.1, 44158.9]

requests_served_4 = [12009.7, 11378.4, 9953.3, 8422.9, 8798.3, 7329.2, 7477.3, 7578.9]
requests_not_served_4 = [0, 0, 1220, 9157.6, 10278.4, 15064.9, 43011.3, 41868.4]

# Configuração do eixo X
x_labels = [100, 200, 400, 600, 800, 1000, 1500, 2000]
x = np.array(x_labels * 4)
x_groups = np.array([x_labels] * 4).flatten()

# Offset para cada grupo no eixo X
offset = len(x_labels)
x1 = np.arange(len(x_labels))
x2 = x1 + offset
x3 = x2 + offset
x4 = x3 + offset

# Criar gráfico de barras empilhadas
fig, ax = plt.subplots(figsize=(14, 8))

bars1 = ax.bar(x1, requests_served_1, width=0.4, label='Requests Served (2 Mec App)', color='blue', hatch='/')
bars2 = ax.bar(x1, requests_not_served_1, width=0.4, bottom=requests_served_1, color='lightblue', label='Requests Not Served (2 Mec App)', hatch='/')

bars3 = ax.bar(x2, requests_served_2, width=0.4, label='Requests Served (4 Mec App)', color='green', hatch='/')
bars4 = ax.bar(x2, requests_not_served_2, width=0.4, bottom=requests_served_2, color='lightgreen', label='Requests Not Served (4 Mec App)', hatch='/')

bars5 = ax.bar(x3, requests_served_3, width=0.4, label='Requests Served (6 Mec App)', color='red', hatch='/')
bars6 = ax.bar(x3, requests_not_served_3, width=0.4, bottom=requests_served_3, color='lightcoral', label='Requests Not Served (6 Mec App)', hatch='/')

bars7 = ax.bar(x4, requests_served_4, width=0.4, label='Requests Served (8 Mec App)', color='purple', hatch='/')
bars8 = ax.bar(x4, requests_not_served_4, width=0.4, bottom=requests_served_4, color='plum', label='Requests Not Served (8 Mec App)', hatch='/')

# Adicionar porcentagens ao lado esquerdo de cada barra
def add_percentages(bars, served, not_served):
    for bar, s, ns in zip(bars, served, not_served):
        total = s + ns
        if total > 0:
            percentage = (s / total) * 100
            # Ajustar a altura do texto
            ax.text(bar.get_x() - 0.1, bar.get_height() + (bar.get_height() * 0.02), f'{percentage:.1f}%', ha='right', va='center', fontsize=10, rotation=90)


add_percentages(bars1, requests_served_1, requests_not_served_1)
add_percentages(bars3, requests_served_2, requests_not_served_2)
add_percentages(bars5, requests_served_3, requests_not_served_3)
add_percentages(bars7, requests_served_4, requests_not_served_4)

# # Adicionar valores às barras
# def add_labels(bars, bottom_values=None, align='left', offset=0.05):
#     for i, bar in enumerate(bars):
#         height = bar.get_height()
#         if bottom_values is None:
#             bottom = 0
#         else:
#             bottom = bottom_values[i]
#         if align == 'left':
#             ax.text(bar.get_x() - offset, bottom, f'{height:.1f}', ha='left', va='bottom', fontsize=9, color='black', rotation=90)
#         elif align == 'right':
#             ax.text(bar.get_x() - offset, bottom + height, f'{height:.1f}', ha='left', va='bottom', fontsize=9, color='black', rotation=90)
#         else:
#             ax.text(bar.get_x() + bar.get_width(), bottom + height, f'{height:.1f}', ha='left', va='bottom', fontsize=9, color='black', rotation=90)

# # Uso
# add_labels(bars1, align='left', offset=0.3)
# add_labels(bars2, requests_served_1, align='right', offset=0.3)
# add_labels(bars3, align='left', offset=0.3)
# add_labels(bars4, requests_served_2, align='right', offset=0.3)
# add_labels(bars5, align='left', offset=0.3)
# add_labels(bars6, requests_served_3, align='right', offset=0.3)
# add_labels(bars7, align='left', offset=0.3)
# add_labels(bars8, requests_served_4, align='right', offset=0.3)

# Configuração do gráfico
ax.set_xlabel('Number of Users', fontsize=14)  # Aumentar o tamanho da fonte
ax.set_ylabel('Number of Requests', fontsize=14)  # Aumentar o tamanho da fonte
ax.set_title('Average Number of Requests Sent', fontsize=16, pad=8)  # Aumentar o tamanho da fonte e ajustar o título
ax.set_xticks(np.concatenate([x1, x2, x3, x4]))
ax.set_xticklabels(x_groups, fontsize=12)  # Aumentar o tamanho da fonte
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), shadow=True, ncol=2, fontsize=14)  # Aumentar o tamanho da fonte na legenda
ax.text(0.10, 1.1, 'i5-10300H', ha='center', va='center', fontsize=14, transform=ax.transAxes)  # Aumentar o tamanho da fonte

plt.xticks(rotation=45)
plt.tight_layout()

# Ajustar a borda superior do gráfico
plt.subplots_adjust(top=0.85)  # Ajuste o valor conforme necessário

# Salvar o gráfico no mesmo diretório onde o script está localizado
plt.savefig('graphs_request_rab_combined_i5.png')

# Exibir o gráfico
plt.show()
