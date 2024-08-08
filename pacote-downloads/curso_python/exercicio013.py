dias = input('Por quantos dias o carro foi alugado? ')
dias = int(dias)

km = float(input('Quantos km rodados? '))

pagar = (dias * 60) + (km*0.15)
print(f'TOTAL A PAGAR: {pagar}')
