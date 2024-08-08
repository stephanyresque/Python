# Herança simples - Relações entre classes

# Associação - usa
# Agregação - tem
# Composição - É dono de
# Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa): #herdei de pessoa
    ...

class Aluno(Pessoa):
    ...

k = Cliente('Stephany', 'Jorge')
l = Aluno('Nathalia', 'Moreno')

k.falar_nome_classe()
l.falar_nome_classe()


