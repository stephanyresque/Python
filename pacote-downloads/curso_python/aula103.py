# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_ordenados = sorted(alunos, key=ordena)

#for aluno in alunos_ordenados:
 #   print(aluno)


"""
aluno = ['a','a', 'a', 'a', 'b', 'c', 'a']
grupos = groupby(sorted(aluno))  #precisa estar em ordem

for chave, grupo in grupos:
    print(chave)
    print(list(grupo))

""" 
grupos = groupby(alunos_ordenados, key=ordena)  

for chave, grupo in grupos:
    print(chave)
    for i in grupo:
         print(i)



