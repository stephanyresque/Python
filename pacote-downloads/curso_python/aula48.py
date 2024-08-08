"""
Funções em python
funções são trechos de código usados para replicar determinada ação ao longo do seu código;
elas podem receber valores para parâmetros (argumentos) e retornar um valor específico;
por padrão, funções python retornam None (nada);

"""

def Ste():
    print('Eu amo ela')

Ste()

def imprimir(a, b, c):   #a, b e c são parâmetros
    print(a+b+c)

imprimir(1, 2, 3)

def saudacao(nome):
    print(f'Olá, {nome}!')

saudacao('Stephany')
