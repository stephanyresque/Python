# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

def recursiva(inicio=0, fim=4):
    print(inicio, fim)
    #caso base:
    if inicio >= fim:
        return fim
    
    #caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())
print()

def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n-1)

print(fatorial(5))


