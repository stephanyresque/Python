
def criar_saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}!'
    return saudar

fala1 = criar_saudacao('Olá')
fala2 = criar_saudacao('Bom dia')

for nome in ['Ste', 'João', 'Nathália']:
    print(fala1(nome))


    
    

