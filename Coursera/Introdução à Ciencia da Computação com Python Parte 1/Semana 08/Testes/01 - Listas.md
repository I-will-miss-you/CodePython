# Listas

1. As listas servem para guardar uma coleção de objetos, que podem ser números, palavras, etc. Quais outros nomes são usados para se referir a listas?
- conjunto
- vetor --» Correto 
- grupo
- array --» Correto 
- coleção

2. Assinale as linhas que criam corretamente uma lista:
- carros = {"Ferrari", "Fusca", "Camry"}
- notas = [3.4, 10, 9.7, 5, 5.9] --» Correto 
- idades = {4, 66, 34, 12, 1, 88}
- aluno = ["Fulano de Tal", 25, "Rua xyz, 123", "São Paulo", "Matemática", 7.5, "Português", 6.6] --» Correto 
- cidades = ["Frankfurt", "New York", "Tokio"] --» Correto 
- flores = [margarida, rosa, tulipa, cravo]

3. Deseja-se ver o primeiro elemento da lista denominada carros. Assinale qual dos comandos abaixo executará corretamente o desejado:
- carros{-1}
- carros[-1]
- carros{1}
- carros[0] --» Correto 
- carros[1]
- carros{0}

4. Deseja-se ver o último elemento da lista denominada carros, na qual existem 5 elementos. Assinale qual(quais) dos comandos abaixo executará(ão) corretamente o desejado:
- carros{-1}
- carros[5]
- carros{4}
- carros{5}
- carros[4] --» Correto 
- carros[-1] --» Correto 

5. O quê o programa abaixo faz?
```py
flores = ["margarida", "rosa", "tulipa", "cravo"]
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=", ")
    tam = tam – 1
```
- imprime os três primeiros elementos na ordem apresentada dentro da lista: margarida, rosa, tulipa
- imprime todos os elementos na ordem apresentada dentro da lista: margarida, rosa, tulipa, cravo
- imprime os três últimos elementos na ordem inversa: cravo, tulipa, rosa
- imprime os três últimos elementos na ordem apresentada dentro da lista: rosa, tulipa, cravo
- imprime os três primeiros elementos na ordem inversa: tulipa, rosa, margarida
- imprime todos os elementos na ordem inversa: cravo, tulipa, rosa, margarida --» Correto 

6. Analise a lista abaixo e assinale as alternativas CORRETAS:
```py
aluno = ["Fulano de Tal", 25, "Rua xyz, 123", "São Paulo", 3, "Matemática", 7.5, "Português", 6.6, "Artes", 10]
```
- o comando type(aluno[4]) dará como resposta que o tipo de dado do valor da posição 4 é um inteiro: <class 'str'>
- o comando aluno[1] = aluno[1] + 1 irá substituir o valor 25, que está na segunda posição, pelo 26 --» Correto 
- o comando type(aluno[-1]) dará como resposta que o tipo de dado do valor da posição 10 é um inteiro: <class 'int'> --» Correto 
- o comando len(aluno) retornará o valor 10, sendo que a contagem dos elementos da lista, em Python, começa em zero
- o comando type(aluno[1]) dará como resposta que o tipo de dado do valor da posição 1 é um inteiro: <class 'int'> --» Correto 
- Esta lista está errada pois é formada por mais de um tipo de dado. Para ela ser válida, todos os elementos deveriam estar entre aspas duplas
- Esta lista é formada por mais de um tipo de dado --» Correto 

7. Assinale a afirmação INCORRETA:
- para criar uma lista vazia em Python é só atribui [] para o nome da lista. Exemplo: nomes = []
- type é uma função que recebe como parâmetro um valor e retorna o tipo deste valor. Por exemplo, se a função type recebe como parâmetro o nome de uma lista e a posição de um elemento dela, será retornado o tipo deste elemento
- a função append irá acrescentar um elemento no início da lista --» Incorreto
- len é uma função que recebe como parâmetro o nome de uma lista e retorna a quantidade de elementos existentes nesta lista

8. Assinale as alternativas que poderiam ser usadas para alterar o último elemento da lista abaixo:
```py
animais = ["gato", "cachorro", "vaca", "cavalo", "casa"]
```
- animais[5] = "cobra"
- animais[-1] = "cobra" --» Correto 
- animais.append = "cobra"
- len(animais[4] = "cobra")
- animais.append("cobra")
- animais[4] = "cobra" --» Correto 