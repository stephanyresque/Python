nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))
media = (nota1 + nota2)/2

if(media < 5):
    print(f'A média entre as notas {nota1} e {nota2} é {media}')
    print('O aluno está reprovado')
elif(media > 5 and media <= 6.9):
    print(f'A média entre as notas {nota1} e {nota2} é {media}')
    print('O aluno está de recuperação')
else:
    print(f'A média entre as notas {nota1} e {nota2} é {media}')
    print('O aluno está aprovado')

