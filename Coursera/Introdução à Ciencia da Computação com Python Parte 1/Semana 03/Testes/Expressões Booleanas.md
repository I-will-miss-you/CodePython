# Expressões Booleanas

1. Assumindo que x está definido como um número inteiro, qual expressão booleana abaixo está escrita de forma correta e que sempre retornará True?
- (-10 < x < 0)
- (x != 0) and (x == 0)
- True and (4 => 3)
- (x > 0) or (x <= 0)  --» Correto 
- not (x > 0) and (x > 0) 

2. No Python, o operador relacional de igualdade é:
- ==  --» Correto 
- =
- <>
- !=
- ^=

3. Se x = 5 e y = 3, qual será o resultado da expressão abaixo? 
```py
x > y
```
- 3
- True  --» Correto 
- Sim
- False
- 5

4. Se x = 5, y = 3 e z = 7, qual será o resultado da expressão abaixo? 
```py
x > y and x < z
```
- 4
- não
- 6
- False
- True --» Correto 

5. Qual o resultado do trecho abaixo?
```py
idade=15
maioridade=18
pode_dirigir = idade >= maioridade
print (pode_dirigir)
```
- True
- 18
- Sim
- False --» Correto 

6. Que tipo de erro ocorre ao executar o comando abaixo, considerando que você tenha acabado de entrar no interpretador Python?
```py
fruta = laranja
```
- SyntaxError.
- TypeError.
- NameError. --» Correto 
- ValueError.

7. Qual a saída gerada pelo trecho de programa abaixo?
```py
x = 10
y = 15
z = 25
print(x == z - y and z != y - x or not y != z - x)
```
- False
- Undefined
- True --» Correto 
- SyntaxError

8. Considere x = 10, y = 20 e z = 30, assinale quais das alternativas abaixo resultam em True:
- print(not y > 10 or not z > 10)
- print(not y < 10 or not z == 10) --» Correto 
- print(x >= 10 or y != z - x) --» Correto 
- print(x <= 30 and y >= 5) --» Correto 

9. Assinale as opções que identificam os nomes dos tipos de dados em Python:
- bool --» Correto 
- str --» Correto 
- float --» Correto 
- int --» Correto 
- True
- SyntaxError
- 10
- Booleano

10. Assuma que a = 1 e b = 2. Qual declaração é verdadeira (True)?
- a != 2 or b == 1 --» Correto 
- a != 1 or b == 1
- not (a == 1)
- a == 2 and b != 1