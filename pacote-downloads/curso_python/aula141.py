# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class MinhaString(str):
    def upper(self):
        print('Chamou o upper')
        return super().upper()

string = MinhaString('Stephany')
print(string.upper())
print('-----------')

class A:
    def __init__(self, atributo):
        self.atributo = atributo

    atributo_a = 'a'

    def metodo(self):
        print('A')

class B(A):
    def __init__(self, atributo, outro):
        super().__init__(atributo)
        self.outro = outro

    atributo_b = 'b'
    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'c'
    def metodo(self):
        super(B, self).metodo()
        super(C, self).metodo()
        print('C')

c = C('atributo', 'outra')
b = B('valor', 'outroo')
print(b.atributo)
print(c.atributo)
print(c.outro)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)

c.metodo()

