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
print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    result = "Abaixo do Peso"
elif imc < 25:
    result = "Peso Ideal"
elif imc < 30:
    result = "Sobrepeso"
elif imc < 40:
    result = "Obesidade"
else:
    result = "Obesidade mórbida"

print(f'Você esta: {result}.')
