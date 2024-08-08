import datetime

ano = int(input('Em qual ano você nasceu: '))

idade = (datetime.date.today().year) - ano

print(f'Quem nasceu em {ano} possui {idade} anos em {datetime.date.today().year}')

if(idade < 18):
    tempo = 18 - idade
    print(f'Falta {tempo} anos para o seu alistamento')
    ano_alist = (datetime.date.today().year) + tempo
    print(f'Seu ano de alistamento será em {ano_alist}')

elif(idade == 18):
    print('Você deve se alistar imediatamente.')

elif(idade > 18):
    tempo = idade - 18
    print(f'Você já deveria ter se alistado há {tempo} anos.')
    ano_alist = (datetime.date.today().year) - tempo
    print(f'O seu ano de alistamento foi em {ano_alist}')

