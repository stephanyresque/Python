"""
Retorno de valores de funções (return);
não posso colocar nada abaixo de return, pois indica que "acaba" a função;

"""


def sub(x, y):
    if x > 10:
        return [x, y]
    else:
        return x - y

print(sub(3, 2))
print(sub(12, 14))

