import os
import matplotlib.pyplot as plt
import numpy as np

# Data
requests_served_1 = [29183.9, 29373.8, 23736.1, 20770.9, 21275.6, 17151.8, 16836.1, 17119.8]
requests_not_served_1 = [0, 0, 3857.1, 19273.8, 26092.4, 40809.7, 101884.9, 96668.8]

requests_served_2 = [27469.4, 25325.8, 22600.2, 19100.3, 19988.6, 15683.8, 16669.7, 17228]
requests_not_served_2 = [0, 0, 2745.5, 20239.3, 23819.4, 36254.7, 97242.5, 95019]

requests_served_3 = [25347.6, 23548.7, 21045.7, 17458.7, 18367.2, 15561.2, 15536.3, 16014.5]
requests_not_served_3 = [0, 0, 2884.4, 18888.5, 21913.2, 36146.2, 91026, 88614.3]

requests_served_4 = [23685, 22100.8, 19086.1, 16598.3, 17773.5, 15108.8, 14838.2, 14912.1]
requests_not_served_4 = [0, 0, 2337.7, 18306.5, 20822.7, 31336.4, 84836, 82163.8]

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
plt.savefig('graphs_request_plmn_combined_i5.png', dpi=300)  # Aumentar a resolução para uma melhor qualidade

# Exibir o gráfico
plt.show()
