# Classe Conta Bancária.
# Crie uma classe chamada ContaBancaria que tenha atributos como
# titular, saldo e métodos para depositar e sacar dinheiro.

class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'seu saldo: {self.saldo}')

    def conta(self):
        print(f'O titular dessa conta é {self.titular} e seu saldo é de {self.saldo}')

    def depositar(self, dinheiro):
        self.saldo += dinheiro


    def sacar(self, valor):
        if valor > self.saldo:
            print('você não pode sacar esse valor.')
        self.saldo -= valor

guilherme = ContaBancaria('guilherme', 0)
guilherme.depositar(50)
guilherme.mostrar_saldo()

guilherme.sacar()
guilherme.mostrar_saldo()