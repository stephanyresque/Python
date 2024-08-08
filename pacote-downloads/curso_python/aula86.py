# raise - lançando exceções (erros);

#print('oi')
#raise ValueError('deu erro')
#print('oiii')

#def divide(n, d):
#    try:
#        return n/d
#    except ZeroDivisionError:
#        return('Tende ao infinito')

#def divide(n, d):
#    if d == 0:
#        raise ZeroDivisionError('Tende ao infinito')
#    else:
#        return n/d

def nao_pode_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    
def deve_ser_num(n):
    tipo = type(n)
    if not isinstance(n, (int, float)):
        raise TypeError(
            'Você não digitou inteiros ou float\n'
            f'{tipo} enviado'
            )
    
def divide(n, d):
    deve_ser_num(n)
    deve_ser_num(d)
    nao_pode_zero(d)
    return n / d


print(divide('8', 2))


