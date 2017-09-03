# Objetos na Memória
1. Considerando os termos usados na programação com Python, assinale as afirmações CORRETAS:
- O objeto é guardado dentro da memória e uma variável guarda o endereço de memória onde o ele está armazenado, ou seja, a variável aponta para a posição de memória onde o objeto está armazenado. --» Correto
- Um byte é composto por 8 bits e 1 bit é representado por 0 ou 1. --» Correto
- Em Python, strings são imutáveis. --» Correto
- Objetos são os comandos que damos para alterar algum dado dentro da memória.
- Memória do computador é uma sequência muito longa de bytes. --» Correto
- Objetos são dados, estruturas de dados que queremos armazenar e funções que vão manipular estes dados. --» Correto
- Byte é a parte da memória onde são armazenados os dados que estamos trabalhando. --» Correto

2. Observe as linhas de comandos abaixo:
```py
lista1 = ["carro", "barco"]
lista2 = lista1
lista3 = [lista1] * 3
lista4 = lista1 * 3
```

Assinale as alternativas CORRETAS:

- A lista 3 terá o seguinte conteúdo ["carro", "barco", "carro", "barco", "carro", "barco"].
- A lista 3 terá o seguinte conteúdo [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]]. --» Correto
- A lista 4 terá o seguinte conteúdo [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]].
- A lista1 terá o seguinte conteúdo ["carro", "barco"]. --» Correto
- A lista 2 terá o seguinte conteúdo ["carro", "barco"]. --» Correto
- A lista 2 terá o seguinte conteúdo [["carro"], ["barco"]].
- A lista 4 terá o seguinte conteúdo ["carro", "barco", "carro", "barco", "carro", "barco"]. --» Correto

3. Observe as linhas de comandos abaixo:
```py
lista1 = ["carro", "barco"]
lista2 = [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]]
lista3 = ["carro", "barco", "carro", "barco", "carro", "barco"]
lista1[1] = "metrô"
```

Assinale as alternativas CORRETAS:

- A lista1 terá o seguinte conteúdo ["carro", "metrô"]. --» Correto
- A lista 2 terá o seguinte conteúdo [["carro", " metrô"], ["carro", " metrô"], ["carro", " metrô"]].
- A lista 3 terá o seguinte conteúdo [["carro", " metrô"], ["carro", " metrô"], ["carro", " metrô"]].
- A lista1 terá o seguinte conteúdo ["carro", "barco"].
- A lista 3 terá o seguinte conteúdo ["carro", " metrô", "carro", " metrô", "carro", " metrô"].
- A lista 3 terá o seguinte conteúdo [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]].
- A lista 2 terá o seguinte conteúdo ["carro", "barco", "carro", "barco", "carro", "barco"].
- A lista 2 terá o seguinte conteúdo ["carro", " metrô", "carro", " metrô", "carro", " metrô"].
- A lista 3 terá o seguinte conteúdo ["carro", "barco", "carro", "barco", "carro", "barco"]. --» Correto
- A lista 2 terá o seguinte conteúdo [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]]. --» Correto

4. Observe as linhas de comandos abaixo:
```py
lista1 = ["carro", "barco"]
lista2 = [lista1] * 3
lista3 = lista1 * 3
lista1[1] = "metrô"
```

Assinale as alternativas CORRETAS:

- A lista1 terá o seguinte conteúdo ["carro", "metrô"]. --» Correto
- A lista 2 terá o seguinte conteúdo ["carro", " metrô", "carro", " metrô", "carro", " metrô"].
- A lista 3 terá o seguinte conteúdo [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]].
- A lista 2 terá o seguinte conteúdo [["carro", " metrô"], ["carro", " metrô"], ["carro", " metrô"]]. --» Correto
- A lista 3 terá o seguinte conteúdo [["carro", " metrô"], ["carro", " metrô"], ["carro", " metrô"]].
- A lista 2 terá o seguinte conteúdo [["carro", "barco"], ["carro", "barco"], ["carro", "barco"]].
- A lista 2 terá o seguinte conteúdo ["carro", "barco", "carro", "barco", "carro", "barco"].
- A lista 3 terá o seguinte conteúdo ["carro", " metrô", "carro", " metrô", "carro", " metrô"].
- A lista1 terá o seguinte conteúdo ["carro", "barco"].
- A lista 3 terá o seguinte conteúdo ["carro", "barco", "carro", "barco", "carro", "barco"]. --» Correto