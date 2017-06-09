# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com o desconto que o usuario quiser de desconto!
import sys

#Função Calc
def calc():
    try:
        preco = float(input('Digite o preço de um produto: '))
        desconto = float(input('Digite o desconto que quer: '))
        precoFinal = preco - ((preco * desconto) / 100)
        print('O produto que antes custava {:.2f}€, com {:.2f}% '
              'desconto, custa agora {:.2f}€ \n\n'.format(preco,desconto, precoFinal))

    except: #caso ocorra um erro - tenta inserir um string em vez de um float
        print('Erro nos valores de entrada')

    else: #caso não ocorra um erro
        return precoFinal

#Função Sair
def sair():
    x = input('Deseja repetir?[s/n]').lower()
    if (x == 's'):
        print('Reiniciando programa... \n\n')
    else:
        print('Encerrando programa... \n\n')
        sys.exit() #termina o programa

#Função "principal"
def main():
    print('{:=^36}'.format(' Desafio #012_1 '))

    while 1:
        calc()
        sair()


#iniciar
main()