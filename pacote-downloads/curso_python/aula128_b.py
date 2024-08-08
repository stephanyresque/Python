import json
from aula128_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])

print(p1.nome, p1.idade)



