'''
Desafio 054

Crie um programa que leia o ano de nascimento de sete pessoas. 
No final mostre quantas pessoas ainda não atingiram a 
maioridade e quantas já são maiores. 
'''
from datetime import date
atual = date.today().year

tot_maior = 0
tot_menor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        tot_maior += 1
    else:
        tot_menor += 1

print(f'Ao todo tivemos {tot_maior} pessoas maiores de idade')
print(f'E também tivemos {tot_menor} pessoas menore de idade')