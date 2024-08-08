#POO em py;

# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes. -> começar com letra maiúscula

"""
um exemplo de classe é a string;
a classe da string é a 'str', nela podemos gerar objetos e ter métodos;
ex:
string = 'Stephany' # a classe é str e o objeto/instancia é 'Stephany'
como método, temos a função upper, lower....

"""
class Pessoa:
    ...

p1 = Pessoa() #criei um novo objeto/instância
p1.nome = 'Stephany'
p1.sobrenome = 'Resque' #atrelei dois atributos a minha classe

p2 = Pessoa() #criei outro objeto/instância
p2.nome = 'Nathália'
p2.sobrenome = 'Moreno'

print(p1)
print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
