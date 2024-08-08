import random

opcoes = [i for i in range(0,6)]
numero = random.choice(opcoes) #tambem poderia usar o randint(0,5)

voce = int(input('Estou pensando em um número entre 0 e 5 ... qual é esse número: '))
if voce == numero:
    print('Você acertou')
else:
    print(f'Você errou, eu pensei em {numero}')


