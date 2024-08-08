import random

print('Suas opções:\n[1] pedra\n[2] papel\n[3] tesoura\n')
opcoes_maquina = [1, 2, 3]
opcao_maquina = random.choice(opcoes_maquina)

opcao_jogador = int(input('Selecionar: '))

if(opcao_maquina == 1):
    print('Opção computador: pedra')
    if(opcao_jogador == 1):
        print('Opção jogador: pedra')
        print('EMPATE')
    elif(opcao_jogador == 2):
       print('Opção jogador: papel')
       print('Vitória: jogador') 
    elif(opcao_jogador == 3):
       print('Opção jogador: tesoura')
       print('Vitória: computador') 

elif(opcao_maquina == 2):
    print('Opção computador: papel')
    if(opcao_jogador == 1):
        print('Opção jogador: pedra')
        print('Vitória: computador')
    elif(opcao_jogador == 2):
       print('Opção jogador: papel')
       print('EMPATE') 
    elif(opcao_jogador == 3):
       print('Opção jogador: tesoura')
       print('Vitória: jogador') 

elif(opcao_maquina == 3):
    print('Opção computador: tesoura')
    if(opcao_jogador == 1):
        print('Opção jogador: pedra')
        print('Vitória: jogador')
    elif(opcao_jogador == 2):
       print('Opção jogador: papel')
       print('Vitória: computador')
    elif(opcao_jogador == 3):
       print('Opção jogador: tesoura')
       print('EMPATE') 

    