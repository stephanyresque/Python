frase = 'conheci a nathália no dia 30 de julho'

i = 0
s = 0
m = ''
while i < len(frase):
    letra = frase[i]

    if letra == ' ':
        i = i + 1
        continue

    qtd = frase.count(letra)
    if s < qtd:
        s = qtd
        m = letra

    i = i + 1

print(f'A letra "{m}" apareceu mais vezes ({s}).')


