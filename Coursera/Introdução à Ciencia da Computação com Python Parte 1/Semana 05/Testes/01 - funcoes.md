# Funções

1. Qual será o resultado apresentado pelo programa abaixo?
- multiplica(4,5)
- 20
- Dará um erro de sintaxe --» Correto 
- 4 * 5 = 20

2. O que o código abaixo irá imprimir?
- x = 10 e y = 20 --» Correto 
- Todas as opções estão erradas
- x = 20 e y = 10
- x = 20 e y = 20
- x = 10 e y = 10

3. Assinale qual (ou quais) das opções abaixo apresenta a função que retorna a soma dos comprimentos de 3 palavras ou frases:
- Errada 
```py 
def total_Caracteres (x, y, z):
return len(x,y,z) 
```
- Errada
```py
def total_Caracteres (x, y, z):
    return sum(len(x)+len(y)+len(z))
```
- Certa
```py
def total_Caracteres (x, y, z):
    return len(x)+len(y)+len(z)
```
- Errada
```py
def total_Caracteres (x, y, z):
    return sum(len(x,y,z))
```

4. O quê a função abaixo retorna? O que é math?
```py
import math

def suspense(x):
    return math.sqrt(x)
```

- Retorna o quadrado de x. "math" é uma função
- Retorna a raiz quadrada de x. "math" é um módulo --» Correto 
- Retorna o quadrado de x. "math" é um módulo
- Retorna a raiz quadrada de x. "math" é uma função
- Todas as opções estão erradas.

5. Se você tivesse que resolver o seguinte exercício:

"Desenvolva uma função que retorne um número lido, maior que zero",

qual(is) das opções abaixo resolveria(m) seu problema?

- Errada
```py
leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x
```
- Errada
```py
leitura():
    x = -1
    while x > 0:
        x = int(input("Digite um valor: "))
    return x
```

- Certa
```py
def leitura():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x
```
- Certa
```py
def leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x
```

```py
def leitura():
    x = -1
    while x > 0:
        x = int(input("Digite um valor: "))
    return x
```
6. Assinale as afirmações CORRETAS:
- A função pode ou não retornar valor --» Correto 
- O nome da função deve representar a tarefa que ela irá executar --» Correto 
- return é usado para a função devolver um determinado valor para quem a chamou --» Correto 
- A função pode receber ou não parâmetros --» Correto 
- Parâmetros de uma função são valores que ela recebe para trabalhar --» Correto 