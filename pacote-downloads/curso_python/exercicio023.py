frase = str(input('Digite algo: ')).strip().lower()

print(f'A letra A apareceu {frase.count('a')} vezes')
print(f'A primeira letra A apareceu na posição {frase.find('a')+1}')
print(f'A última letra A aparece na posição {frase.rfind('a')+1}')




