import math
ang = float(input('ÂNGULO: '))
ang = math.radians(ang)
seno = math.sin(ang)
cos = math.cos(ang)
tag = math.tan(ang)

print(f'SENO: {round(seno, 2)}')
print(f'COSSENO: {round(cos, 2)}')
print(f'TANGENTE: {round(tag, 2)}')


