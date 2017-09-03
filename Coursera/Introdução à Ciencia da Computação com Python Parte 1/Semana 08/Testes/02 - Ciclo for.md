# Ciclo For

pontos
1. Qual afirmação abaixo define corretamente o “for” da linguagem Python?
- “for” é uma estrutura de seleção que serve para selecionar elementos de uma lista
- “for” é o comando que serve para tornar a lista vazia
- “for” é uma variável que serve para guardar uma lista
- “for” é uma estrutura de repetição e serve, entre outras coisas, para percorrer uma lista --» Correto 
- “for” é um comando que serve para criar uma lista

2. Abaixo é apresentada a estrutura do “for”:
```
for <variável> in <conjunto de valores>:
    <comandos>
```
Assinale a afirmação correta:
- <variável> receberá valores numéricos, sempre iniciando pelo valor 0 (zero), um em cada interação. <conjunto de valores> deve ser uma lista numérica. <comandos> são os comandos que serão executados enquanto houver valores para a <variável> assumir.

- <variável> receberá os valores existentes no <conjunto de valores>, um em cada interação. <conjunto de valores> poderá ser uma lista ou um intervalo de valores. <comandos> são os comandos que serão executados enquanto houver valores para a <variável> assumir. --» Correto 

- <variável> receberá valores numéricos, sempre iniciando pelo valor 0 (zero), um em cada interação. <conjunto de valores> poderá ser uma lista ou um intervalo de valores. <comandos> são os comandos que serão executados quando o comando “for” finalizar.

- <variável> receberá os valores existentes no <conjunto de valores>, um em cada interação. <conjunto de valores> poderá ser uma lista ou um intervalo de valores. <comandos> são os comandos que serão executados quando o comando “for” finalizar.

3. Assinale os trechos de códigos que imprimem todos os elementos da lista abaixo:

    ``` animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"] ```

- Errado
```py
for x in animais:
    print("--> ", x-1)
```

- Correto 
```py
for x in animais:
    print("--> ", x)
```

- Correto 
```py
for x in range(len(animais)):
    print("--> ", animais[x])
```

- Correto 
```py
for x in animais:
    print("--> " + x)
```

- Errado 
```py
for x in range(len(animais)):
    print("--> ", x)
```

4. Assinale as afirmações corretas:
- O código abaixo imprimirá os valores da lista pares da posição 5 até a posição 10, ou seja, 12, 14, 16, 18, 20, 22. --> Errado
```py
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(5, 10):
    print(pares[x])
```

- O código abaixo imprimirá todos os valores da lista pares. --» Correto 
```py
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(len(pares)):
    print(pares[x])
```

- O código abaixo imprimirá os múltiplos de 5, começando por 0 e terminando com 45. --» Correto 
```py
for i in range(0, 50, 5):
	print(i)
```

- O código abaixo imprimirá todos os valores da lista pares. --» Errado
```py
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(len(pares)):
    print(x)
```

- Os comandos abaixo imprimirão os valores: 16, 13, 10, 7. --» Correto 
```py
for i in range(16,4,-3):
	print(i)
```

5. O código abaixo gera uma lista de números. Analise-o:
```py
valores = []
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)
```
Assinale o código que gera uma lista com os mesmos valores gerados acima:

- Errado
```py
valores = []
for i in range(1, 10):
    valores.append(i+1)
```

- Errado
```py
valores = []
for i in range(0, 10, 2):
    valores.append(i)
```

- Correto 
```py
valores = []
for i in range(2, 10, 2):
    valores.append(i)
```

- Errado
```py
valores = []
for i in range(1, 10, 2):
    valores.append(i)
```

6. Assinale as alternativas que mudam o valor “papagaio” para “piriquito” da lista abaixo:

    ``` animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"] ```

- animais("papagaio") = animais("piriquito")
- animais[2] = animais.append("piriquito")
- animais.append("papagaio","cobra")
- animais[2] = "piriquito" --» Correto 
- animais[3] = "piriquito"
- animais[-3] = "piriquito" --» Correto 
- animais[1+1] = "piriquito" --» Correto 