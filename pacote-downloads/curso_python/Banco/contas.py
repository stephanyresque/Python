import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float =0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...

    def depositar(self, valor: float) -> float:
        self.saldo = self.saldo + valor
        self.detalhes(f'DEPÓSITO {valor:.2f}')
        return self.saldo
    
    def detalhes(self, msg: str = '' ) -> None:
        print(f'Seu saldo é {self.saldo:.2f} {msg}')
        print('--------')
    
    def __repr__(self):
        class_nome = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_nome}, {attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor:.2f}')
            return self.saldo
        
        print('Não foi possível realizar o saque')
        self.detalhes(f'SAQUE NEGADO {valor:.2f}')
        return self.saldo   

class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float =0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite


    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE {valor:.2f}')
            return self.saldo
        
        print('Não foi possível realizar o saque')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO {valor:.2f}')
        return self.saldo   
    
    def __repr__(self):
        class_nome = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_nome}, {attrs}'



if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222)
    cp1.sacar(10)
    cp1.depositar(100)
    cp1.sacar(10)
    print('#############')
    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(10)
    cc1.sacar(90)
    cc1.sacar(1)
    
