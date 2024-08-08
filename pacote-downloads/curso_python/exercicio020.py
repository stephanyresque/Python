import math
numero = int(input('Informe um número de no máximo quatro casas: '))


milhar = math.trunc(numero/1000)
centena = math.trunc((numero - (milhar*1000))/100)
dezena = math.trunc((numero - (milhar*1000)-(centena*100))/10)
unidade = numero - (milhar*1000)-(centena*100) - (dezena*10)


print(f'milhar: {milhar}')
print(f'centena: {centena}')
print(f'dezena: {dezena}')
print(f'unidade: {unidade}')

