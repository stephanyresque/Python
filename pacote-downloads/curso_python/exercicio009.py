comp = input('Informe o comprimento da parede: ')
larg = input('Informe a largura: ')
comp = float(comp)
larg = float(larg)

area = comp * larg
print(f'A parede tem dimensão de {comp}x{larg} com {area}m2.')
print(f'Será necessário {area/2} litros de tinta.')
