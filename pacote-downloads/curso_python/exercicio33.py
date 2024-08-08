casa = (input('Valor da casa: '))
sal = (input('Salário: '))
anos = (input('Anos de prestação: '))
casa = float(casa)
sal = float(sal)
anos = int(anos)

prestacao = casa/(anos*12)
if prestacao <= (sal*0.3):
    msg = 'PERMITIDO'
else:
    msg = 'NEGADO'

print(f'Prestação de R${round(prestacao, 2)} para {anos} anos\nAcesso {msg}.')


