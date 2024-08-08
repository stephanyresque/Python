"""
Escopo de funções;
escopo significa o local onde aquele código pode atingir;
existe o escopo global e local;
global é o escopo onde todo o código é alcançável;
local é o escopo onde apenas nomes do mesmo local podem ser alcançados;

"""

x=1

def escopo():
    x = 10
    def outra():
        x = 11
        y = 2
        print(x, y)

    outra()
    print(x)

print(x)
escopo()
print(x)
print('---------------\n')

z=1

def escopo():
    global z
    z = 10
    def outra():
        z = 11
        w = 2
        print(z, w)

    outra()
    print(z)

print(z)
escopo()
print(z)