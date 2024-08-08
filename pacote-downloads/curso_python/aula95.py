#Decoradores são "Syntax Sugar";

def criar_func(func):
    def interna(*args):
        for arg in args:
            is_string(arg)

        resultado = func(*args)
        return resultado
    return interna

@criar_func
def inverte_string(string):
    #print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    



invertida = inverte_string('STEPHANY')
print(invertida)
