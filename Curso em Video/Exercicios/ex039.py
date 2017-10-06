'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar. 
- Se já passou do tempo do alistamento. 

Seu programa também deverá mostrar o tempo que falta ou
que passou do prazo.
'''
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))

idade = ano_atual - ano_nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(
    ano_nascimento, idade, ano_atual))

if idade == 18:
    print('Você tem que se alistar imediatamente.')
elif idade < 18:
    anos_em_falta = 18 - idade
    print('Ainda falta {} anos para o alistamento'.format(anos_em_falta))
    ano_alistamento = ano_atual + anos_em_falta
    print('O seu alistamento será em {}'.format(ano_alistamento))
else: # idade > 18
    anos_passados = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(anos_passados))
    ano_alistamento = ano_atual - anos_passados
    print('O seu alistamento foi em {}.'.format(ano_alistamento))