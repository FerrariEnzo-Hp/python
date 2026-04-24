class ContaBancaria:
    """
    cria uma conta bancaria e permite fazer saques e depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'conta criada com sucesso\nid:{self.id}\ntitular:{self.titular}\nsaldo:{self.saldo}')



    def __str__(self):
        return f'Conta de id {self.id}, pertence a {self.titular} e possui R${self.saldo:,.2f} em conta'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'{self.titular} depositou R${valor:,.2f} na conta de id {self.id}')
    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            print(f'{self.titular} sacou R${valor:,.2f} na conta de id {self.id}')
        else:
            print('saque negado')


c1 = ContaBancaria(125, "Jorge", 2500)
c1.depositar(1000)
c1.sacar(500)
print(c1)