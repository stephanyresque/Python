"""
argumento nomeado tem nome com sinal de igual
argumento não nomeado recebe apenas o argumento (valor)

"""

def sub(x, y):
    print(f'a subtração entre {x} e {y} é {x - y}')

sub(3, 2)

sub(y=2, x=3) #nomeado, outra forma

# posso fazer assim tbm: sub(3, y=2), mas só no final.

"""
valores padrão para parametros;
ao definir uma função, parametros podem ter valores padrão;
caso o valor não seja enviado para o parametro, o valor padrão será usado;

"""
def soma(x, y, z=None): #sempre no final, nunca no meio ou início
    if z is not None:
        print(f'{x=} {y=} {z=}', x+y+z)
    else:
        print(f'{x=} {y=}', x+y)

soma(2, 4)
soma(1, 4, 6)


