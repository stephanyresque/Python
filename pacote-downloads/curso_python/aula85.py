# try, except, else e finally;

try:
    a = 10
    b = 0
    print('tentando'[100])
    c = a/b
    print('consegui')
except ZeroDivisionError:
    print('dividiu por zero')
except NameError:
    print('variável não declarada')
except (TypeError, IndexError) as error:
    print('Type error + Index error')
    print(f'TIPO DE ERRO: {error}')
    print(f'TIPO DE ERRO: {error.__class__.__name__}')
except Exception:
    print('Erro desconhecido')

print('continuando')

# o finally sempre será executado, mesmo se ocorrer um erro;

try:
    print(1)
finally:
    print(2)



