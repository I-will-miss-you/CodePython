
#Parte teorica
'''
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')

print('Carro novo' if tempo <= 3 else 'Carro velho')
'''

#Parte Pratica
'''
nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('O seu nome é tão normal!')
print('Bom dia, {}'.format(nome))
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua média foi boa! Parabéns')
else:
    print('Sua média foi ruim! Estude Mais!')

print('Parabéns' if m >= 6 else 'Estude Mais!')
