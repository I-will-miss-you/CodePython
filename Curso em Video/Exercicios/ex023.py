# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex: Digite um número: 1834
# Unidade: 4
# Dezena:  3
# Centena: 8
# milhar:  1
num = int(input('Informe um número: '))
#n = str(num)
#print('Analisando o número {}'.format(num))
#print('Unidade: {}'.format(n[3]))
#print('Dezena: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))