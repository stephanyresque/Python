# mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False, fotografando=False):
        self.nome = nome
        self.filmando = filmando
        self.fotografando = fotografando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return
        
        print(f'{self.nome} está filmando')
        self.filmando = True
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} está filmando no momento')
            return
        print(f'{self.nome} está fotografando')
        self.fotografando = True



c1 = Camera('Sony')
c2 = Camera('Canon')
c1.filmar()
c2.fotografar()

#print(c1.filmando)
#print(c2.filmando)