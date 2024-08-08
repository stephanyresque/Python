# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('HEY')

    @classmethod
    def pessoa_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def anonima(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('Stephany', 20)
print(Pessoa.ano)
Pessoa.metodo_de_classe()

p2 = Pessoa.pessoa_50_anos('Lucimar')
print(p2.nome, p2.idade)

p3 = Pessoa.anonima(24)
print(p3.nome, p3.idade)



