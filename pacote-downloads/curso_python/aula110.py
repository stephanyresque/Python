# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\steph\\OneDrive\\Documentos\\curso_python\\'
caminho_arquivo += 'aula110.txt'

#arquivo = open(caminho_arquivo, 'w')
#
#arquivo.close()
with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('linha 01\n')
    arquivo.write('linha 02\n')
    arquivo.writelines(
        ('linha 03\n', 'linha 04\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    arquivo.seek(0, 0)
    print('lendo')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip()) 
    print(arquivo.readline().strip()) 
    print('Readlines agora:')
    arquivo.seek(0, 0)
    for linhas in arquivo.readlines():
        print(linhas.strip())

print(10*'#')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

