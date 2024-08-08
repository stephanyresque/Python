import random

lista_alunos = []

def alunos():
    nome = input('NOME DO ALUNO: ')
    lista_alunos.append(nome)

for i in range(0, 4):
    alunos()

escolhido = random.choice(lista_alunos)
print(f'ALUNO ESCOLHIDO: {escolhido}')


