
pontos = 0
resp1 = input('Quanto é 2+2?\na) 2\nb) 3\nc) 4\nd) 5\nSua resposta: ')

if resp1 == '4':
    print('Você acertou!')
    pontos = pontos + 1
else:
    print('Você errou.')

resp2 = input('Quanto é 5 x 5 ?\na) 10\nb) 30\nc) 15\nd) 25\nSua resposta: ')

if resp2 == '25':
    print('Você acertou!')
    pontos = pontos + 1
else:
    print('Você errou.')

resp3 = input('Quanto é 2^3 ?\na) 10\nb) 4\nc) 8\nd) 12\nSua resposta: ')

if resp3 == '8':
    print('Você acertou!')
    pontos = pontos + 1
else:
    print('Você errou.')

print(f'FIM DE JOGO\nVocê acertou {pontos} de 3 questões')
