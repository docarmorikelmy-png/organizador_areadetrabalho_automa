
import os
import shutil

# 1. Caminho da pasta que queremos organizar
pasta = r'C:\Users\silva\OneDrive\Desktop'

# 2. Categorias e extensões
categorias = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'],
    'PDFs': ['.pdf'],
    'Documentos': ['.doc', '.docx', '.txt', '.odt'],
    'Planilhas': ['.xls', '.xlsx', '.csv', '.ods'],
    'Apresentacoes': ['.ppt', '.pptx', '.odp'],
    'Musicas': ['.mp3', '.wav', '.flac', '.aac'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Compactados': ['.zip', '.rar', '.7z', '.tar', '.gz']
}

# 3. Cria as pastas das categorias
for categoria in categorias:
    caminho_pasta = os.path.join(pasta, categoria)
    os.makedirs(caminho_pasta, exist_ok=True)

# 4. Pega tudo que existe na Área de Trabalho
arquivos = os.listdir(pasta)

# 5. Analisa cada arquivo
for arquivo in arquivos:

    caminho_arquivo = os.path.join(pasta, arquivo)

    # Ignora pastas
    if not os.path.isfile(caminho_arquivo):
        continue

    # 6. Descobre a extensão
    extensao = os.path.splitext(arquivo)[1].lower()

    # 7. Verifica em qual categoria a extensão se encaixa
    for categoria, extensoes in categorias.items():

        if extensao in extensoes:

            # 8. Cria o caminho de destino
            destino = os.path.join(pasta, categoria, arquivo)

            # 9. Move o arquivo
            shutil.move(caminho_arquivo, destino)

            print(f'{arquivo} → {categoria}')
            break

print('Organização concluída!')
