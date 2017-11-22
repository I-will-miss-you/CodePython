'''
Desafio 056

Desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres tem menos de 20 anos.
'''
soma_idade = 0
maior_idade_homem = 0
qtd_mulheres_menor_20 = 0

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    # Soma das idades
    soma_idade += idade

    # Homem mais velho e seu nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    # Mulher com menos de 20 anos
    if sexo in "Ff" and idade < 20:
        qtd_mulheres_menor_20 += 1


media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos')
print(f'O homem mais velho tem {maior_idade_homem} anos e chama-se {nome_homem_mais_velho}')
print(f'Ao todo são {qtd_mulheres_menor_20} mulheres com menos de 20 anos')
