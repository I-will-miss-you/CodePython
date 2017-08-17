# Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo

class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo if saldo > 0 else 0
        self.limite = limite


    def sacar(self, valor):
        if self.saldo - valor < self.limite:
            return False
        else:
            self.saldo -= valor
            return True

    def depositar(self, valor):
        if valor < 0:
            return False
        else:
            self.saldo += valor
            return True

    def getSaldo(self):
        return self.saldo


    def __str__(self):
        return self.cliente.__str__() + "\nSaldo: " + str(self.saldo)

