'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- À vista dinheiro / cheque:    10% de desconto
- À vista no cartão:             5% de desconto
- em até 2x no cartão:          preço normal
- 3x ou mais no cartão:         20% de juros
'''
print(f"{ ' LOJAS GUANABARA ' :=^40}")

preço = float(input('\nPreço das compras: R$'))
print(''' 
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opção = int(input('Qual é a opção: '))

erro = False
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.005)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opção == 4:
    total = preço + (preço * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}x de R${parcela:.2f}')
else:
    total = 0
    print('Opção Inválida de pagamento. Tente novamente.')
    erro = True

if not erro:
    print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f}.')
