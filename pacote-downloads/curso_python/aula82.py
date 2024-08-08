#Generator functions in py;
#função geradora, uma função que sabe pausar;

def generator(n=0):
    yield 1 #pausar
    print('continuando...')
    yield 2 #pausar
    print('mais uma vez...')
    yield 3 #pausar
    print('agora sim')
    yield 4 #pausar

gen = generator(n=0)
print(next(gen))
print()
print(next(gen))
print()
for n in gen:
    print(n)