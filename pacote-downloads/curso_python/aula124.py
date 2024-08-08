
class Animal:
    def __init__(self, nome):
        self.nome = nome
        variavel = 'valor'
        print(variavel)

    def acao(self, alimento):
        return f'{self.nome} está comendo {alimento}'


gato = Animal('Gatinho')
print(gato.nome)
print(gato.acao('ração'))


        
