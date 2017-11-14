'''
Desafio 055

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos. 
'''
for i in range(1,6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maior = menor = peso
    else:
        maior = peso if peso > maior else maior
        menor = peso if peso < menor else menor


print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')      
