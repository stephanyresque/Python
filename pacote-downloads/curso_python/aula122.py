# Métodos em instâncias de classes python;

class Carro:
    def __init__(self, nome):
        self.nome = nome
    
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
celta = Carro('Celta')

print(fusca.nome)
#print(fusca.acelerar()) dessa forma retorna none, logo nem sempre é bom usar o print;
fusca.acelerar()
print(celta.nome)
celta.acelerar() #nesse caso, desta forma é melhor;


