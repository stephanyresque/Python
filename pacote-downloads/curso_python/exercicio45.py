
tot = 0
soma = 0
for num in range(1, 500):
    if(num%2 != 0 and num%3==0):
        tot = tot + 1
        soma = soma + num

print(f'A soma dos {tot} número solicitados é {soma}')