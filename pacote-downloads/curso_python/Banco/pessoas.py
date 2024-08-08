import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade
    
    def __repr__(self):
        class_nome = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_nome}, {attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None 



if __name__ == '__main__':
    c1 = Cliente('Stephany Resque', 20)
    c1.conta = contas.ContaCorrente(777, 444, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Nathalia Moreno', 20)
    c2.conta = contas.ContaPoupanca(888, 333, 100)
    print(c2)
    print(c2.conta)
    
