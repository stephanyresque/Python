# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

def soma(*args):
    print(sum(args))

soma(1,2,3)

def soma_2(a, b, /):
    print(a +b)

#soma_2(1, b=2) -> isso dá erro
soma_2(1,2)

def soma_3(a, b, /, x, y):
    print(a+b+x+y)

soma_3(1,2,3,y=4)

def soma_4(a, b, *, c):
    print(a+b+c)

soma_4(1,2,c=3) #dps do * DEVE ser nomeado