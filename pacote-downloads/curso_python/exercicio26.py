velocidade = float(input('Qual a velocidade do veículo[km/h]: '))

if velocidade <= 80:
    print('Tenha um bom dia.')
else:
    multa = 7*(velocidade-80)
    print(f'Limite excedido!\nMultado no valor: R${multa}')