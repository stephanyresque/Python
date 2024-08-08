lado1 = float(input('Informe o lado: '))
lado2 = float(input('Informe o lado: '))
lado3 = float(input('Informe o lado: '))

if ((lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1+lado2)):
    print('Triângulo possível')
    if(lado1 == lado2 and lado2 == lado3):
        print('TIPO: equilátero')
    elif ((lado1 == lado2 and lado1 != lado3) or (lado2 == lado3 and lado2 != lado1) or (lado3 == lado1 and lado3 != lado2)):
        print('TIPO: isóceles')
    else:
        print('TIPO: escaleno')
else:
    print('Triângulo não possível')

