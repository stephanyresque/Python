# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Caneta:

    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor
    
    
caneta = Caneta('azul')
# getter -> obter um valor
print(caneta.cor)
caneta.cor = 'rosa' #-> quero fazer algo assim
print(caneta.cor)
