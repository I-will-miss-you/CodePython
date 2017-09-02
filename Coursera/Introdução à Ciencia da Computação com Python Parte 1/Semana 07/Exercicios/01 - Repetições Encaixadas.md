# Repetições Encaixadas

1. Analise o código abaixo:
```py
x = 1
cont = 0
while x < 3:
    y = 0
    while y <= 4:
        # Iteração
        y = y + 1
    x = x + 1
```
Quantas vezes o programa executará a linha 6?
- 2
- 10 --» Correto 
- Nenhuma
- 7
- 5

2. Assinale a forma correspondente à saída gerada pelo programa abaixo:
```py
def desenha(linha):    
    while linha > 0:
        coluna = 1
        while coluna <= linha:
            print('*', end = "")
            coluna = coluna + 1
        print()
        linha = linha - 1

desenha(5)
```
- Errada
```
    *
   **
  ***
 ****
*****
```

- Errada
```
*****
 ****
  ***
   **
    *
```

- Correta
```
*****
****
***
**
*
```

- Errada
```
*
**
***
****
*****
```

- Errada
```
*****
*****
*****
*****
*****
```

3. Qual(is) trecho(s) abaixo completam corretamente o programa para que ele imprima a tabuada de 1 a 10?
```py
def tabuada():
    # parte faltante

tabuada()
```
- Correto
```py
tab = 0
while tab < 10:
    tab = tab + 1
    i = 0
    while i < 10:
        i = i + 1
        print(tab,"x",i,"=",tab*i)
    print()
```

- Errado
```py
tab = 1
i = 1
while tab <= 10 and i <= 10:
    print(tab,"x",i,"=",tab*i)
    i = i + 1
    tab = tab + 1
print()
```

- Correto
```py
tab = 1
while tab <= 10:
    i = 1
    while i <= 10:
        print(tab*i, end = "\t")
        i = i + 1
    print()
    tab = tab + 1
```

- Errado
```py
tab = 1
while tab <= 10:
    i = 1
    print(tab*i, end = "\t")
    i = i + 1
    print()
    tab = tab + 1
```

- Correto
```py
tab = 1
while tab <= 10:
    i = 1
    while i <= 10:
        print(tab,"x",i,"=",tab*i)
        i = i + 1
    print()
    tab = tab + 1
``` 

4. Analise o código abaixo e assinale a resposta correta para a seguinte pergunta: Quantas vezes a linha 6 será executada?
```py
x = 2
cont = 0
while x >= 0:
    y = 0
    while y >= 4:
        #comando qualquer
        y = y + 1
    x = x - 1
```
- 3
- Nenhuma vez --» Correto 
- 15
- Infinitas vezes
- 12

5. Analise o código abaixo e assinale a resposta correta para a seguinte pergunta: Quantas vezes a linha 6 será executada?
```py
x = 2
cont = 0
while x >= 0:
    y = 0
    while y <= 4:
        #comando qualquer
        y = y - 1
    x = x - 1
```
- Infinitas vezes --» Correto 
- Nenhuma vez
- 15
- 3
- 12

6. Foi desenvolvido um programa em Python para desenhar um quadrado como este abaixo:
```
******
*    *
*    *
*    *
******
```
Porém, o programa não está executando a tarefa desejada. Analise o código abaixo e assinale a opção que indica o que precisa ser alterado para que ele desenhe o quadrado solicitado.
```py
altura = 5
linha = 1
while linha <= altura:
    print("*", end = "")
    coluna = 2
    while coluna < altura: 
        if linha == 1 or linha == altura:
            print("*")
        else:
            print(end = " ")
        coluna = coluna + 1
    print("*")
    linha = linha + 1
```
- Nenhuma das alternativas resolve o problema
- Na linha 4 não existe o "end = """. O correto na linha 4 é:

``` print("*") ```

- linha 8 está errada, deveria ser:

``` print("*", end = "\t") ```

- Na linha 12 faltou "end = """. O correto na linha 12 é:

``` print("*", end = "") ```

- linha 8 está errada, deveria ser: --» Correto

``` print("*", end = "") ``` 

- Não deve existir as linhas 9 e 10, referentes ao else

7. O programa abaixo irá imprimir os números 1, 2, 2 e 4.

    Em qual formato esses valores serão impressos?
```py
x = 1
while x < 3:
    y = 1
    while y < 3:
        print(x*y, end = "\t")
        y = y + 1
    x = x + 1
```
- Correto
<pre>
1   2   2   4
</pre>
- Errado
<pre>
1 2 2 4 
</pre>  
- Errado
<pre>
1
    2
        2
            4
</pre>
- Errado
<pre>
1
2   
2
4
</pre>
