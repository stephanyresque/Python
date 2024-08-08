
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *var):
    return funcao(*var)

v = executa(saudacao, 'Boa tarde', 'Stephany')

print(v)