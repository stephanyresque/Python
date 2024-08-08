#Atributos de classe
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Stephany', 20)
p2 = Pessoa('Nathália', 14)
print(p1.ano_nascimento())
print(p2.ano_nascimento())
print(Pessoa.ano_atual)