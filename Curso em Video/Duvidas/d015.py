# Validar n Primo

num = int(input('Numero: '))
#vamos supor que entra sempre um número inteiro

# range(2, num + 1) -> inicio no '2'  e vai até 'num' inclusive
# se não adicionares um ele para no numero 'num - 1'
for i in range(2, num + 1):
    # o número é divisivel por um número que não é ele mesmo
    if num % i == 0 and num != i:
        print('Número não é primo')
        break
    # não ocorreu a condição enterior e i é igual ao numero inserido
    elif num == i:
        print('Número é primo')

    #Outra forma de fazer parecida com a anterior
for i in range(2, num + 1):
    if num % i == 0:
        print('Número não é primo')
        break
    elif num == i:
        print('Número é primo')