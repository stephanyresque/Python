
perguntas = [
    {   
        'questao':'Quanto é 2+2?',
        'opçoes': ['1', '3', '4', '5'],
        'resposta': '4',
    },
    {
        'questao': 'Quanto é 5 x 5?',
        'opçoes':['10', '25', '15', '100'],
        'resposta': '25',
    },
    {
        'questao': 'Quanto é 2^3?',
        'opçoes': ['8', '4', '12', '24'],
        'resposta': '8',
    }
]

pontos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['questao'])
    print()

    for i, item in enumerate(pergunta['opçoes']):
        print(f'{i})', item)
    resp = input('Sua resposta: ')
    if resp == pergunta['resposta']:
        print('ACERTOU!')
        pontos = pontos + 1
    else:
        print('ERROU..')


    print()

print(f'FIM DE JOGO\nACERTOS: {pontos} de 3')






        
