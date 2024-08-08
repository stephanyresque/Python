import os
lista_compras = []
opc_pos = 'i, a, l'

while True:
    print('------LISTA DE COMPRAS INTELIGENTE------')
    print('Selecione as opções abaixo: ')
    opc = input('[i]tem, [a]pagar, [l]istar: ')

    if opc == 'i':
        os.system('cls')
        item = input('Item adicionado: ')
        lista_compras.append(item)
        for n ,j in enumerate(lista_compras):
            print(n, j)
            
    elif opc == 'a':
        os.system('cls')
        indice_str = input('Posição do item: ')
        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except:
            print('Não há itens nessa posição.')

    
    elif opc == 'l':
        os.system('cls')
        for n, j in enumerate(lista_compras):
            print(n, j)

    if opc not in opc_pos:
        print('Por favor selecione uma das opções.')
    
    if opc == 'l' and len(lista_compras) == 0:
        print('Não há itens para listar ainda.')

    
        
        
    
