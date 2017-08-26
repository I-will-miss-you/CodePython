num = int(input("Digite um número inteiro: "))
prime = True
i = 2
while i < num and prime:
    if(num % i == 0):
        prime = False
    i += 1

print("primo" if prime else "não primo") 
