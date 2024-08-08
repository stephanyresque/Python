from dataclasses import dataclass

@dataclass( order=True)
class Pessoa:
    nome: str
    sobrenome: str



if __name__ == '__main__':
    lista = [Pessoa('C','Z'), Pessoa('B','X'), Pessoa('A','Y')]
    ordena = sorted(lista, key=lambda p:p.sobrenome)
    print(ordena)


    
