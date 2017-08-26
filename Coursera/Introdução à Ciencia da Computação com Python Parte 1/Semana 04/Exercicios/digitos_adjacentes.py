num = int(input("Digite um número inteiro: "))
igual = False

anterior = num % 10
num = num // 10
while num > 0 and not igual:
    novo = num % 10
    if(anterior == novo):
        igual = True
    else:
        anterior = novo
    num = num //10

print("sim" if igual else "não") 
