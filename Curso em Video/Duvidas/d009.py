try:
    nome = input('Digite o seu nome')
except ValueError:
    print('Dados inválidos')
else:
    print(nome)

