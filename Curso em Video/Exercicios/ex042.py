'''
Refaça o Desafio 035 dos triângulos acrescentando o recusrso de mostrar 
que tipo de triângulo será formado:

- Equilátero: todos os lados iguais.
- Isósceles: dois lados iguais. 
- Escaleno: todos os lados diferentes. 
'''

reta1 = float(input('Reta 1: '))
reta2 = float(input('Reta 2: '))
reta3 = float(input('Reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        triangulo = "EQUILÁTERO"
    elif reta1 != reta2 != reta3 != reta1:
        triangulo = "ESCALENO"
    else:
        triangulo = "ISÓSCELES"
    print(f'As retas formam um triângulo {triangulo}')
else:
    print('As retas nao formam um triângulo')