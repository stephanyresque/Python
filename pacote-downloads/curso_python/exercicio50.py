nome = str(input('Digite a frase/nome: ')).strip().upper()

palavras = nome.split()
palavras_juntas = ''.join(palavras)
inverso = ''
for letra in range(len(palavras_juntas) - 1, -1, -1):
    inverso += palavras_juntas[letra]

if inverso == palavras_juntas:
    print(palavras_juntas, inverso)
    print('palíndromo')
else:
    print(palavras_juntas, inverso)






