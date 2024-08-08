"""
init inicializa os atributos da minha classe;
quando criamos uma função dentro da classe ela é chamada de método;
"""

class Pessoa:
    def __init__(self, nome, sobrenome): #sua instância está na self, ela referencia, neste exemplo, a p1;
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Stephany', 'Resque') 
#p1.nome = 'Stephany'
#p1.sobrenome = 'Resque' 

p2 = Pessoa('Nathália', 'Moreno') 
#p2.nome = 'Nathália'
#p2.sobrenome = 'Moreno'


print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)