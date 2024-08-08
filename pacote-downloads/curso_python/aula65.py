"""
sets são eficientes para remover valores duplicados de iteráveis
seus valores serão sempre únicos
não aceitam valores mutáveis
não tem índexes
não garatem ordem
são iteráveis

"""

s1 = {1,1,1,2,3,4,4,4,5,5,}
print(s1, type(s1))

l1 = [1,2,3,4,4,4,5,5,5,6,6]
l1 = set(l1)
l2 = list(l1)
print(l2)

s2 = {1,2,3,4}
print(3 in s2)
print(7 not in s2)
for numero in s2:
    print(numero)

s3 = set('Ste')
for letra in s3:
    print(letra)
