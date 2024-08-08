hora = input('Olá, que horas são? ')

try:
    mom = int(hora)
    if mom >= 0 and mom <= 11:
        print(f'Bom dia, {mom} horas.')

    elif mom > 11 and mom <= 17:
        print(f'Boa tarde, {mom} horas')
    
    elif mom > 17 and mom <= 23:
        print(f'Boa noite, {mom} horas')

    else:
        print('Não conheço essa hora.')
except:
    print('Você não informou a hora.')