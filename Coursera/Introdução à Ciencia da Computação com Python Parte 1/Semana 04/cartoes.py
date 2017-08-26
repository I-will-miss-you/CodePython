meuCartao = int(input("Digite o número do seu cartão de crédito: "))

encontrei = False
cartãoLido = 1
while cartãoLido == 0 and not encontrei:
    cartãoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartãoLido == meuCartao:
        encontrei = True

if encontrei:
    print("EBA! Meu cartão está lá!")
else:
    print("Xi, meu cartão não está lá...")
