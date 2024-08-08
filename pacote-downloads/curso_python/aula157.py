# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome):
        print(nome,'esta chamando...', self.phone)
        

call1 = CallMe('62999984656')
call1('Stephany')
