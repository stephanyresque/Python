from dataclasses import dataclass,field

@dataclass
class Pessoa:
    nome: str = field(
        default= 'not sent'
    )
    sobrenome: str = 'not sent'
    idade: int = 0
    endereco: list[str] = field(default_factory=list)



if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)