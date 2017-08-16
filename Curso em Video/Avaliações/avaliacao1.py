'''
1 - Originalmente, o nome da Linguagem Python foi dado pelo grupo de criação para homenagear algo. É uma referência a:
    -   um animal: a serpente
    -   um dos programadores, que tinha o sobrenome Python
    -   um animal: o pato
    --> um grupo de comédia Inglês
    -   um personagem de desenho animado

 2 - A Linguagem Python tem várias características. Entre os itens a seguir, qual é o único que não representa uma característica da Linguagem Python?
    -   batteries included
    -   orientada a objetos
    -   multiplataforma
    --> focada em propósitos específicos
    -   fácil e intuitiva

 3 - Se por acaso estivermos escrevendo um programa em Linguagem Python e quisermos adicionar funcionalidades que não estão presentes no momento, como proceder?
    -   devemos escrever todas as funcionalidades adicionais, uma a uma
    -   devemos pedir para um outro programador desenvolver para nós
    --> podemos importar um módulo que tenha esta funcionalidade implementada
    -   só podemos escolher outra linguagem de programação, que tenha mais funcionalidades
    -   não há nada a se fazer

 4 - Imagine que você tenha uma variável chamada “nomeCliente” em um programa Python e que ela tenha uma string armazenada nela.
  Qual seria o comando necessário para saber quantas letras esse nome tem ao todo?
    --> len(nomeCliente)
    -   nomeCliente.len
    -   nomeCliente.len()
    -   len.nomeCliente()
    -   nomeCliente().len()

 5 - Você está escrevendo um programa e precisa de uma funcionalidade especial: fazer seu programa parar por alguns
 segundos e depois voltar às atividades normais. Qual das linhas abaixo você deve escrever no início do seu código?
    -->   from time import sleep
    -   from sleep import time
    -   from wait import time
    -   from time import wait
    -   import wait

 6 - Conhecendo bem o funcionamento dos operadores aritméticos da Linguagem Python e a ordem de precedência na
 execução desses operadores dentro de uma expressão, qual será o valor final da variável “res” na expressão:

    res = 5 * 3 ** 2
    print(res)

    --> 45
    -   225
    -   30
    -   0
    -   acontecerá um erro! ** não existe

 7 - Considere o seguinte trecho de código escrito em Linguagem Python:

    nome = 'Gustavo Guanabara'
    print(nome.split())

    Ao executar essas instruções, o resultado exibido na tela será:
    -   Gustavo Guanabara
    -   GustavoGuanabara
    --> ['Gustavo', 'Guanabara']
    -   Gustavo/Guanabara
    -   ['Gustavo'], ['Guanabara']

 8 - Considere as instruções a seguir, escritas em Python 3:

    num = 4.999
    print(int(num))

    Ao executar essas instruções, o que aparecerá na tela?
    --> 4
    -   5
    -   4.5
    -   5.0
    -   vai aparecer um erro

 9 - Considerando a técnica de fatiamento de strings, analise as linhas a seguir:

    nome = 'Joao dos Anjos Moura'
    print(nome[1:10:2].upper())

    Qual será o resultado exibido na tela após a execução desses comandos?
    -   JAO
    -   OAO DOS A
    -   JOAO DOS A
    --> OODSA
    -   OODSAJ

 10 - Considere as seguintes instruções, em Linguagem Python:

    n1 = '7'
    n2 = 4
    print(n1 + str(n2))

    O que vai aparecer na tela, quando executarmos esse programa?
    -   Vai aparecer um erro
    --> Vai aparecer o valor 74
    -   Vai aparecer o valor 11
    -   Não vai aparecer nada
    -   O programa vai travar

 11 - Analise atentamente as seguintes atribuições, feitas em Linguagem Python:

    frase = 'Curso em Video de Python'
    separado = frase.split()
    palavra = separado[2]
    letra = palavra[3]
    print(letra.upper())

    Ao executar os comandos acima, o que será exibido na tela?
    --> E
    -   EM
    -   VID
    -   H
    -   PYTH

 12 - Considerando a importação do módulo datetime usando a instrução a seguir:

    from datetime import date

    A partir daí, como criamos uma variável “ano”, que conterá o ano atual, configurado no sistema?
    -   ano = datetime.date.year
    -   ano = date.year.today()
    -   ano = date.today.year()
    --> ano = date.today().year
    -   ano = datetime.today.year

 13 - Considere o código a seguir:

    from random import randint
    num = randint(1, 6)
    res = num // 2
    print(res)

    Podemos executar esse mesmo código várias vezes e podemos ter vários resultados diferentes para a variável “res”.
    Quais são as possibilidades de resultado?
    -   1, 2 ou 3
    --> 0, 1, 2 ou 3
    -   1, 2, 3, 4, 5 ou 6
    -   o código acima está com erro
    -   é impossível definir os resultados possíveis

 14 - Considere a seguinte estrutura condicional composta desse trecho de código escrito em Python:

    if preço < 1000:
        novo = preço + 50
    else:
        novo = preço - 35

    Uma outra maneira de representar o código acima, usando apenas uma linha e que gere o mesmo resultado seria:
    --> novo = preço + 50 if preço < 1000 else preço - 35
    -   novo = if preço < 1000 preço + 50 else preço - 35
    -   novo = +50 if preço < 1000 else +35
    -   novo = preço+50: preço+35 if preço < 1000
    -   novo = preço+50 if preço <1000: else: preço+35

 15 - Considere o código a seguir:

    from random import choice
    n = [2, 5, 9, 1, 4]
    res = choice(n) % n[0]
    print(res)

    Podemos executar esse mesmo código várias vezes e podemos ter vários resultados diferentes para a variável “res”. Quais são as possibilidades de resultado?
    --> 0 ou 1
    -   2, 5, 9, 1 ou 4
    -   5, 9, 1 ou 4
    -   0, 1 ou 2
    -   não é possível definir as possibilidades
'''

from random import choice

n = [2, 5, 9, 1, 4]
res = choice(n) % n[0]
print(res)