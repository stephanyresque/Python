
caminho_arquivo = 'C:\\Users\\steph\\OneDrive\\Documentos\\curso_python\\'
caminho_arquivo += 'aula111.txt'

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção')