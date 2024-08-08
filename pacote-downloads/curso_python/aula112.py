import os

caminho_arquivo = 'C:\\Users\\steph\\OneDrive\\Documentos\\curso_python\\'
caminho_arquivo += 'aula112.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('linhaaaaa 01')

#os.remove(caminho_arquivo)
os.rename(caminho_arquivo, 'aula112-2.txt')