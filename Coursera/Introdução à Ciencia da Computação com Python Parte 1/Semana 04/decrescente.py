decrescente = True
valor = anterior = int(input("Digite o primeiro número da sequência: "))
while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("A sequência está em ordem decrescente! :-)")
else:
    print("A sequência não está em ordem decrescente! :-(")
