num = int(input('Informe um número: '))
cont = 0
for i in range(1, num+1):
    if(num%i==0):
        print(f'{i} divide {num}')
        cont = cont + 1

if(cont == 2):
    print(f'O número {num} é dividido {cont} vezes, então ele é PRIMO =)')
else:
    print(f'O número {num} é dividido {cont} vezes, então ele NÃO é PRIMO =(')
