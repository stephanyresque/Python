veloc = 55
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1


if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE):
    print('O carro passou pelo radar 1.')
    if veloc > RADAR_1:
        print('Velocidade excedida')
        print('MULTADO')
    else:
        print('Velocidade permitida.')
        print('SEGUIR.')
else:
    print('Carro fora da zona do radar.')
