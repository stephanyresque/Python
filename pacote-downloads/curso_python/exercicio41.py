def menu():
    print('------LOJA DA BIZU------')
    print('[0] à vista com dinheiro/cheque')
    print('[1] à vista com cartão')
    print('[2] até 2x no cartão')
    print('[3] a partir de 3x no cartão')

preco = float(input('Valor do produto: '))
menu()
forma = int(input('Selecione a fomra de pagamento: '))
if forma == 0:
    preco_final = round(preco * 0.9, 2)
    print(f'Produto no valor de R${preco} sairá por R${preco_final}')
elif forma == 1:
    preco_final = round(preco * 0.95, 2)
    print(f'Produto no valor de R${preco} sairá por R${preco_final}')
elif forma == 2:
    parcelas = int(input('Quantas parcelas: '))
    preco_parcela = preco/parcelas
    print(f'Produto no valor de R${preco} sairá por {parcelas} parcelas de R${preco_parcela}')
else:
    parcelas = int(input('Quantas parcelas: '))
    preco_final = preco*1.2
    preco_parcela = preco_final/parcelas
    print(f'Produto no valor de R${preco} sairá por {parcelas} parcelas de R${preco_parcela}\nVocê pagará no final o total de R${preco_final}')