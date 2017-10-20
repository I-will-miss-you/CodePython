'''
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu 
IMC e mostre seu status de acordo com a tabela abaixo:

- Abaixo de 18.5:   Abaixo do Peso
- Entre 18.5 e 25:  Peso Ideal
- Entre 25 até 30:  Sobrepeso
- Entre 30 até 40:  Obesidade
- Acima de 40:      Obesidade mórbida
'''
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é o seu peso? (m) '))

imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em SOBREPESO MÓRBIDA, cuidado!')

