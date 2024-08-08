# problema dos parâmetros mutáveis;

def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Stephany')
adiciona_clientes('Nathália', cliente1)
cliente2 = adiciona_clientes('Pedro')
adiciona_clientes('João', cliente2)
adiciona_clientes('Felipe', cliente2)
print(cliente1)
print(cliente2)
print()
# da forma acima, nunca terei listas separadas, a mesma lista ficará sendo reutilizada;
# segue abaixo o jeito certo:

print(30*"*")
print()

def adicionar_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

clientes_1 = adicionar_cliente('Stephany')
adiciona_clientes('Nathália', clientes_1)
adicionar_cliente('Marcus', clientes_1)
clientes_2 = adicionar_cliente('Pedro')
adicionar_cliente('João', clientes_2)
adicionar_cliente('Felipe', clientes_2)
print(clientes_1)
print(clientes_2)


