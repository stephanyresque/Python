# classes decoradoras
class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10
    
    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador

@Multiplicar
def somar(x, y):
    return x + y

dois = somar(2,2)
print(dois)
