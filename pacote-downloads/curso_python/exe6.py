# 710.888.991-96     replace tira e substitui por algo
#    3   7   11

import re
import sys

# cpf = '710.888.991-96'.replace('.', '').replace('-', '').replace(' ', '')

entrada = input('Informe seu CPF: ')
cpf = re.sub(r'[^0-9]', '',entrada )

entrada_seq = entrada == entrada[0] * len(entrada)
if entrada_seq:
    print('Você digitou dados sequenciais.')
    sys.exit()


nove_dig = cpf[:9]
soma = 0
cont_1 = 10
for digito in nove_dig:
    soma = soma + (int(digito) * cont_1)
    cont_1 = cont_1 - 1


valor = (soma * 10) % 11
primeiro_digito = valor if valor <= 9 else 0

dez_dig = nove_dig + str(primeiro_digito)
soma_2 = 0
cont_2 = 11
for digito in dez_dig:
    soma_2 = soma_2 + (int(digito) * cont_2)
    cont_2 = cont_2 - 1 



valor_2 = (soma_2 * 10) % 11
segundo_digito = valor_2 if valor_2 <= 9 else 0

novo_cpf = f'{nove_dig}{primeiro_digito}{segundo_digito}'


if cpf == novo_cpf:
    print(f'CPF {cpf} válido')
else:
    print(f'CPF {cpf} inválido.')
