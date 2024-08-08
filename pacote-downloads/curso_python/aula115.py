
print('-----------LISTA DE TAREFAS INTELIGENTE-----------')

lista = []
lista_desfeitos = []


def mostrar_lista(lista):
    print('-----SUAS TAREFAS-----')
    for a in lista:
        print(a)
    print(22*'-')
    print()


def lista_tarefas(acao):
    if acao != 'desfazer' and acao != 'listar' and acao != 'refazer':
        lista.append(acao)
        mostrar_lista(lista)
    
    if acao == 'desfazer':
        if lista == []:
            print('A lista está vazia')
        else:
            lista_desfeitos.append(lista[-1])   
            lista.pop()
            mostrar_lista(lista)

    if acao == 'listar':
        mostrar_lista(lista)
    
    if acao == 'refazer':
        if lista_desfeitos == []:
            print('Não há o que refazer')
            mostrar_lista(lista)
        else:
            lista.append(lista_desfeitos[-1])
            lista_desfeitos.pop()
            mostrar_lista(lista)

while True:
    print('Adicione uma tarefa ou informe um comando possível\nComandos: listar, desfazer, refazer, sair.')
    fazer = str(input('Sua ação: ')).strip().lower()
    if fazer == 'sair':
        print('Você saiu. Tenha um bom dia =)')
        break
    print()
    lista_tarefas(fazer)








