# Listas dentro de lista
salas = [
#-------0-------------1--------
    ['Stephany', 'Nathália'], # 0
#------0-------1-----------------
    ['Gab', 'Jack'],  # 1
#-----0----1----2-------------3------------
    ['A', 'B', 'C', (0, 10, 20, 30, 40)] #2
                  #--0---1---2---3---4-----
]
print(salas)
print(salas[0])
print(salas[0][0])
print(salas[0][1])
print(salas[2][3][2])

print('-------------')

for sala in salas:
    print(f'Sala: {sala}')
    for item in sala:
        print(item)
