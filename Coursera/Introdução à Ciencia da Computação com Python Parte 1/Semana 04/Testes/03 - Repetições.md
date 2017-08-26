# Repetições
1. Quantas vezes o código abaixo imprimirá “Olá Mundo!”?
- 8
- 9
- 10
- 11 --» Correto 
- 0

2. O que faz o trecho de programa abaixo?
- imprime apenas os ímpares menores que 10. --» Correto 
- imprime os números de 10 a 0.
- não imprime nada.
- imprime apenas os pares menores que 10.

3. Analise o trecho de programa abaixo e responda: quantas vezes os comandos representados aqui por "iteração" serão executados?
Observe que, se você tentar executar este trecho no interpretador, ele dará erro pois o valor de "n" não está definido. Considere que "n" é uma variável que armazena um valor inteiro positivo e assinale a alternativa correta.
```py
i = 1
while i < n:
    "iteração"
    i = i + 1
```
- n
- 2 * n
- n + 1
- n - 1 --» Correto

4. O que faz o programa abaixo?
```py
terminou = False
p = i = 0
while (not terminou):
    n = int(input("Digite um número, ou zero para terminar: "))
    if n == 0:
        terminou = True
    else:
        if n % 2 == 0:
            p = p + 1
        else:
            i = i + 1

print ("P = ", p)
print ("I = ", i)
```
- Lê dez números e conta a quantidade de números pares e ímpares digitados pelo usuário. No final, imprime o resultado.
- Conta a quantidade de números pares e ímpares digitados pelo usuário e imprime o resultado após o usuário digitar 0 (zero) --» Correto 
- Verifica se um determinado número é par ou ímpar. Caso seja 0 (zero), ele informa ao usuário que ele é neutro.
- De um conjunto de n números, imprime se há números pares e ímpares ou não.