1. Considerando a lista abaixo, assinale as alternativas CORRETAS:

    ``` alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] ```

- o comando “ letras = alfabeto[1:10] “ cria uma lista denominada “letras” com as 10 letras, a partir da “b”, existentes na lista “alfabeto”
- o comando “ alfabeto[13:27] “ mostra as 13 últimas letras do alfabeto (de “n” até “z”) --» Correto 
- o comando “ alfabeto[:13] “ mostra as 13 primeiras letras do alfabeto (de “a” até “m”) --» Correto 
- o comando “ alfabeto[13:] “ mostra as 13 últimas letras do alfabeto (de “n” até “z”) --» Correto 
- o comando “ letras = alfabeto[:] “ cria uma lista denominada “letras” com todos os valores existentes na lista “alfabeto” --» Correto 
- o comando “ len(alfabeto) “ dará como resultado 26 --» Correto 
- o comando “ alfabeto[0:13] “ mostra as 13 primeiras letras do alfabeto (de “a” até “m”) --» Correto 

2. Analise o código abaixo:
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes
carnes2.append("ponta de alcatra") 
```

Assinale a opção que mostra quais serão os valores existentes na lista “carnes” e na “carnes2”.

- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim"]
```
- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
```

- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim"]
```

- Correto
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
```

3. Analise o código abaixo:
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = []
for cns in carnes:
    carnes2.append(cns)
carnes2.append("ponta de alcatra")
```
    Assinale a opção que mostra quais serão os valores existentes na lista “carnes” e na “carnes2”.
- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
```

- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim"]
```

- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim"]
```

- Correto
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
```

4. Analise o código abaixo:
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes[:]
carnes2.append("ponta de alcatra")
```
    Assinale a opção que mostra quais serão os valores existentes na lista “carnes” e na “carnes2”.

- Correto
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
 ```

 - Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
 ```

 - Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim"]
 ```

 - Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim"]
```

5. O quê será impresso pelo código abaixo?
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
if "ponta de alcatra" in carnes:
    print("XXX")
else:
    if "ponta de alcatra" in carnes2:
        print("YYY")
    else:
        print("ZZZ")
```
- ZZZ
- YYY --» Correto 
- XXX

6. O quê existirá dentro de cada uma das três listas após ser executado o código abaixo?
```py
carnes1 = ["picanha", "alcatra"]
carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]
carnes3 = carnes2 + carnes1
```
- Errado
```py
carnes1 = ["filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra"]

carnes3 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
```

- Correto
```py
carnes1 = ["picanha", "alcatra"]

carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]

carnes3 = ["filé mignon", "cupim", "ponta de alcatra", "picanha", "alcatra"]
```

- Errado
```py 

carnes1 = ["filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra"]

carnes3 = ["filé mignon", "cupim", "ponta de alcatra", "picanha", "alcatra"]
```

- Errado
```py
carnes1 = ["picanha", "alcatra"]

carnes2 = ["filé mignon", "cupim", "ponta de alcatra"]

carnes3 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
```

- Errado
```py
carnes1 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]

carnes2 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]

carnes3 = ["picanha", "alcatra", "filé mignon", "cupim", "ponta de alcatra"]
```

7. O quê existirá na lista “x” após serem executadas as linhas de comandos abaixo?
```py
pares = [ 2, 4, 6, 8, 10]
x = pares * 3
```

- x = [ 6, 12, 18, 24, 30]
- x = [ 2, 4, 6, 8, 10]
- x = [ 6, 12, 18, 24, 30, 6, 12, 18, 24, 30, 6, 12, 18, 24, 30]
- x = [ 2, 4, 6, 8, 10, 2, 4, 6, 8, 10, 2, 4, 6, 8, 10] --» Correto 

8. O quê existirá nas listas “carnes” e “x” após serem executadas as linhas de comandos abaixo?
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
x = carnes
del (x[-1])
```

- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]

x = ["picanha", "alcatra", "filé mignon"]
```

- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon", "cupim"]

x = ["picanha", "alcatra", "filé mignon", "cupim"]
```

- Correto
```py
carnes = ["picanha", "alcatra", "filé mignon"]

x = ["picanha", "alcatra", "filé mignon"]
```

- Errado
```py
carnes = ["picanha", "alcatra", "filé mignon"]

x = ["picanha", "alcatra", "filé mignon", "cupim"]
```