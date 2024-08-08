"""
args - argumentos não nomeados
*args - empacotamento e desempacotamento

"""
x, y, *resto = 1,2,3,4,5
print(x, y, resto)

def func(*args):
    total = 0
    for numero in args:
        print(total)
        total = total + numero


func(1,2,3,4)
print()

def soma(*num):
    tot = 0
    for numb in num:
        tot = tot + numb
    return tot

resul = soma(1,5,34,3)
print(resul)

