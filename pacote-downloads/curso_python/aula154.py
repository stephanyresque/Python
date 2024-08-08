from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('ocorreu erro ', e) 
    finally:   
        print('fechando arquivo')
        arquivo.close()


with my_open('aula154.txt', 'w') as arquivo:
    arquivo.write('Linha 01\n')
    arquivo.write('Linha 02\n')
    arquivo.write('Linha 03\n', 124)
    print('WITH', arquivo)

