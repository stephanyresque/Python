

def mul(*num):
    tot = 1
    for numero in num:
        tot = tot * numero
    print(tot)

mul(1,2,3,4,5)

def parimpar(valor):
    if(valor%2 == 0):
        print("PAR")
    else:
        print("ÍMPAR")


parimpar(11)