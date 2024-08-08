iterable = ['eu', 'tenho', '__iter__']
iterator = iter(iterable)

generator = (n for n in range(11))

print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print()

for n in generator:
    print(n)