from PIL import Image

# Carregar as duas imagens
img1 = Image.open("combined_graphs_plmn_2_mec_apps.png")
img2 = Image.open("combined_graphs_plmn_4_mec_apps.png")

# Calcular a largura total (a largura das duas imagens será a mesma)
total_width = img1.width
# Calcular a altura total (a altura será a soma das alturas das duas imagens)
total_height = img1.height + img2.height

# Criar uma nova imagem com a largura e altura calculadas
new_img = Image.new('RGB', (total_width, total_height))

# Colocar a primeira imagem no topo (canto superior esquerdo)
new_img.paste(img1, (0, 0))
# Colocar a segunda imagem abaixo da primeira (no canto superior esquerdo)
new_img.paste(img2, (0, img1.height))

# Salvar a imagem combinada
new_img.save('Grafico_plmn_5_minutos_processamento_2_4_mec_apps.png')
