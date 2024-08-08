salario = float(input('Informe o salário do funcionário: R$'))
if salario > 1250:
    reajuste = salario*1.1
    print(f'Novo salário: R${round(reajuste, 2)}')
else:
    reajuste = salario*1.15
    print(f'Novo salário: R${round(reajuste, 2)}')

