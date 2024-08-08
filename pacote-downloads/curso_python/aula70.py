
def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = executa(
    lambda m: lambda n: n*m,
    2
)
print(duplica(3))
print()
print(
    executa(
        lambda x, y : x + y,
        2, 4
    )
)
print()
print(
    executa(
        lambda *numeros:sum(numeros),
        1,3,5,2,3,4
    )
)
