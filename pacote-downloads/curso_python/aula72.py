pessoa = {
    'nome':'Stephany',
    'sobrenome':'Resque'
}

dados_pessoa = {
    'idade':20,
    'altura':1.64
}

pessoa_completa = {**pessoa,**dados_pessoa}

print(pessoa_completa)
print()
#kwargs = argumentos nomeados;

def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_argumentos_nomeados(1,2, nome='Nat', idade=20)
print()

mostra_argumentos_nomeados(**pessoa_completa) #desempacotou


