import os
import matplotlib.pyplot as plt
import numpy as np

# Dados
requests_served_1 = [17228.2, 15977.6, 12577.2, 11527.9, 11866.6, 9137, 9266.4, 9202.3]
requests_not_served_1 = [0, 0, 254.8, 12180.1, 15939.6, 26919.4, 64819.6, 62059.2]

requests_served_2 = [16048.4, 14644, 10984.7, 11294.3, 11497.6, 8884.6, 9030.9, 9387.9]
requests_not_served_2 = [0, 0, 344.8, 12290.6, 15502.8, 25504.8, 63629.2, 60187.3]

requests_served_3 = [15010.4, 13682.7, 10940.6, 10422.2, 10871.8, 8861.4, 8921.3, 9072.2]
requests_not_served_3 = [0, 0, 360.4, 10998.1, 14473.5, 22788.7, 58357, 57674.4]

requests_served_4 = [14391.4, 13480.4, 10556.9, 9346.3, 10048.4, 8317.8, 8215.3, 8424.5]
requests_not_served_4 = [0, 0, 401.6, 11552.3, 14090.6, 21316.7, 57855.9, 55053.8]

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
ax.set_xlabel('Number of Users', fontsize=14)
ax.set_ylabel('Number of Requests', fontsize=14)
ax.set_title('Average Number of Requests Sent', fontsize=16, pad=20)  # Ajuste o valor do pad conforme necessário
ax.set_xticks(np.concatenate([x1, x2, x3, x4]))
ax.set_xticklabels(x_groups, fontsize=12)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), shadow=True, ncol=2, fontsize=14)
ax.text(0.10, 1.1, 'i7-10510U', ha='center', va='center', fontsize=14, transform=ax.transAxes)

plt.xticks(rotation=45)
plt.tight_layout()

# Ajustar a borda superior do gráfico
plt.subplots_adjust(top=0.85)  # Ajuste o valor conforme necessário

# Salvar o gráfico no mesmo diretório onde o script está localizado
plt.savefig('graphs_request_plmn_combined_i7.png')

# Exibir o gráfico
plt.show()
