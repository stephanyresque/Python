import importlib
import aula89_m

for i in range(10):
    importlib.reload(aula89_m) #estou recarregando o módulo
    print(i)

