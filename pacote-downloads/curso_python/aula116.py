import os

def listar(tarefas):
    print()
    if not tarefas:
        print('Não há tarefas para listar')
        return
    print('Tarefas')
    for tarefa in tarefas:
        print(f'\t{tarefa}')


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Não há tarefas para desfazer')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Não há tarefas para resfazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa')
        return 
    tarefas.append(tarefa)


tarefas = []
tarefas_refazer = []


while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite um comando ou tarefa: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'cls':
        os.system('cls')
        
        continue
    
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue