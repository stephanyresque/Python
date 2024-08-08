# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('José', 18)
# p1.__dict__['outra'] = 'coisa' -> é editável, posso adicionar ou remover coisas
print(p1.__dict__)
print(vars(p1))

dados = {'nome': 'Stephany', 'idade': 20} #tbm é possível
p2 = Pessoa(**dados)
print(vars(p2))

