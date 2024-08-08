
import os 

palavra_secreta = 'nathalia'
letras_acertadas = ''
i = 0
while True:

    letra_digitada = input(f'Digite uma letra ({i}x): ')

    if letra_digitada.isdigit() is True:
        print('Por favor, informe somente letras.')
        continue
    
    if len(letra_digitada) > 1:
        print('Por favor, informe apenas uma letra.')
        continue
     
    i = i + 1

    if letra_digitada in palavra_secreta:
        letras_acertadas = letras_acertadas + letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada = palavra_formada + letra_secreta
        else:
            palavra_formada = palavra_formada + '*'
    
    print('PALAVRA FORMADA: ', palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Você ganhou! A palavra secreta era {palavra_secreta}')
        print(f'Núemro de tentativas: {i-1}')
        letras_acertadas = ''
        i = 0




    
    

