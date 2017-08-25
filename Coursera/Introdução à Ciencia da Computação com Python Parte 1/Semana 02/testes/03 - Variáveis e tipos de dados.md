# Variáveis e tipos de dados

1.  Qual o tipo de dado armazenado na variável x pelo comando abaixo?
```py
x = input ("Qual a idade? ")
```
- booleano, pois o sinal de igualdade é operador relacional
- float (número real), pois considera a idade fracionada do usuário
- inteiro, pois considera apenas a idade completa do usuário
- a função input sempre devolve um string  --»  Correto

2. Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente?
```py
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
a = b
b = a
print(a)
print(b)
```
- a e b serão 2 --» Correto
- a será 2 e b será 1
- a e b serão 1
- a será 1 e b será 2

3. Quais os valores finais das variáveis a e b, se o usuário digitar 1 e 2, respectivamente?
```py
a = int(input("Qual o valor de a? "))
b = int(input("Qual o valor de b? "))
aux = a
a = b
b = aux
print(a)
print(b)
```
- a e b serão 1
- a e b serão 2
- a será 1 e b será 2
- a será 2 e b será 1 --» Correto