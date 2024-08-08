dist = float(input('Qual a distância da viagem[km]: '))

if dist <= 200:
    preco = 0.5 * dist
    print(f'PREÇO A PAGAR: R${preco}')
elif dist > 200:
    preco = 0.45 * dist
    print(f'PREÇO A PAGAR: R${preco}')