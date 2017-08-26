num = int(input("Digite o valor de n: "))
fact = 1
while num > 0:
    fact *= num
    num -= 1
print(fact)