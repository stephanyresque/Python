
cont = 0
soma = 0
for i in range(6):
    num = int(input(f'Informe o {i+1}° número: '))
    if(num%2==0):
        cont = cont + 1
        soma = soma + num

print(f'Houve {cont} pares e a soma entre eles é {soma}')