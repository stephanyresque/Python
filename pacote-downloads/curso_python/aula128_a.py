import json

CAMINHO_ARQUIVO = 'aula128.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Stephany', 20)
p2 = Pessoa('Nathália', 20)
p3 = Pessoa('Marcus', 22)

bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
