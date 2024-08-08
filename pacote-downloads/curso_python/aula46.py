# Operação ternária (condicional de uma linha)
# <valor> if <condição> else <outo valor>

print('valor' if True else 'outro valor')
print('valor' if False else 'outro valor')
cond = 10 == 10
var = 'valor' if cond else 'outro valor'
print('-------------------')
print(var)
print('-------------------')
digito = 10
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
