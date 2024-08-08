
def eu(numero):
    return f'D: {2*numero} \nT: {3*numero} \nQ: {4*numero}'

# print(eu(2))


def multiplicador(valor):
    def multiplicado(num):
        return valor * num
    return multiplicado

n2 = multiplicador(2)
n3 = multiplicador(3)
n4 = multiplicador(4)

print(n4(7))