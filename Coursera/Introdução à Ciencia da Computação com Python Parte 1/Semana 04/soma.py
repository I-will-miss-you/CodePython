
print("Digite uma sequência de valore terminada por zero.")

soma = 0

valor = int(input("Digite um valor a ser somado: "))
while valor != 0:
    soma += valor
    valor = int(input("Digite um valor a ser somado: "))


print("A soma dos valores digitados é: ", soma)
