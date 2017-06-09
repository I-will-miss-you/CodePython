# progama simples
nome = str(input('ola, qual e o seu nome?'))
esc = str(input('você quer ser meu amigo[sim/não]'))
if esc == 'sim':
    print('escolha uma opção {}'.format(nome))
    escolha = str(input("'calculadora' ou 'dialogo'"))
    if escolha == 'calculadora':
        num1 = int(input('escolha um numero'))
        num2 = int(input('escolha mais um numero'))
        r = num1 + num2
        print(' ')
        print('a soma de {} é {} igual a {}'.format(num1, num2, r))
    if escolha == 'dialogo':
        print('ola')
    else:
        print('opção invalida.')
if esc == 'não':
    print(' ok, ate mais.')
    print('deseja reiniciar[sim/não]')
else:
    print('opção invalida')
    print('deseja reiniciar[sim/não]')