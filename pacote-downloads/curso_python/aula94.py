"""
Funçoes decoradoras e decoradores;
decorar = adicionar/remover/restringir/alterar;
funções decoradoras são funções que decoram outras funções;
decoradores são usados para fazer o python usar as funções decoradoras em outras funções;

"""

def criar_func(func):
    def interna(*args):
        for arg in args:
            is_string(arg)

        resultado = func(*args)
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    


inverte_string_checar = criar_func(inverte_string)
invertida = inverte_string_checar(123)
print(invertida)
