
import random
import sys

nove_dig = ''
for i in range(9):
    nove_dig = nove_dig + str(random.randint(0,9))

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

cpf_gerado = f'{nove_dig}{primeiro_digito}{segundo_digito}'

print(cpf_gerado)
