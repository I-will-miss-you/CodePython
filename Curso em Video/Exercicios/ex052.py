'''
Desafio 052

Faça um programa que leia um número e diga 
se ele é ou não um número primo.
'''
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0: 
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end='')

print('\033[m')
print(f'O número {num} foi dividível {tot} vezes.')
print('E por isso ele {}'.format('É PRIMO.' if tot == 2 else 'NÃO É PRIMO.'))
