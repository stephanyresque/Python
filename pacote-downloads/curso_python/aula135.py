# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self.protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        print(self.__private) # posso
        return 'isso tbm é público'
    
    def _metodo_protected(self):
        return 'isso tbm é protegido'

f = Foo()
print(f.public)
print(f.metodo_publico())
# print(f.protected) -> isso não pode
# print(f._metodo_protected()) -> isso tbm não