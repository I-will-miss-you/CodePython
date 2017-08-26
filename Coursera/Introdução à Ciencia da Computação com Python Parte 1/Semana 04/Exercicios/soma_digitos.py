num = int(input("Digite um número inteiro: "))
aux = num
soma = 0
while aux > 0:
    soma += aux % 10
    aux = aux // 10

print(soma)