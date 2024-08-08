"""
métodos em set;
add, clear, update, discard

operadores;
união | união(union) - une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
deferença simétrica ^ - itens que não estão em ambos

"""
s1 = set()
s1.add('Ste') #só adiciona um valor
s1.add(20)
s1.update(('Hello World', 1, 2, 3)) #mais de um valor
s1.discard(3)
print(s1)

s2 = {1,2,3,4}
s2.clear()
print(s2)
