cont = 0

while cont < 100:
    cont = cont + 1
    
    if cont == 6:
        print('Não quero')
        continue
    if cont >= 10 and cont <= 30:
        print(f'NÃO VOU MOSTRAR O {cont}')
        continue

    print(cont)    

    if cont == 40:
        break

print('Acabou')