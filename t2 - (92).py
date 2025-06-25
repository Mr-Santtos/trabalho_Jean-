class ContaBancaria:
    def __init__(self, numero_conta):
        self.numero_conta = numero_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Erro: saldo insuficiente.")
        else:
            self.saldo -= valor
