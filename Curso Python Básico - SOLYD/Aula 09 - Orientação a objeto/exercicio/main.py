'''
    EXERCICIO: Crie um software de gerenciamento bancário
    Esse software poderá ser capaz de criar clientes e contas
    Cada cliente possui nome, cpf, idade
    Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo
'''


from cliente import Cliente
from conta import Conta

cli_1 = Cliente('Luis', '123.456.789-10', 18)

conta_1 = Conta(cli_1, -1500, -500)

#print(cli_1)
print(conta_1)

deposito = 1000
if conta_1.depositar(deposito):
    print('\033[32mDeposito realizado com sucesso.\033[m\nSaldo atual R$ {}'.format(conta_1.getSaldo()))
else:
    print('\033[31mDeposito não foi realizado com sucesso.\033[m\nSaldo atual R${}'.format(conta_1.getSaldo()))

saque = 1501
if conta_1.sacar(saque):
    print('\033[32mO levantamento realizado com sucesso.\033[m\nSaldo atual R$ {}'.format(conta_1.getSaldo()))
else:
    print('\033[31mO levatamento não foi realizado com sucesso.\033[m\nSaldo atual R${}'.format(conta_1.getSaldo()))
