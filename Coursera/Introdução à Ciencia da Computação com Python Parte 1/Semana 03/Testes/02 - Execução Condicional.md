# Execução Condicional

1. O que é impresso ao digitar: 1 + 1 + 1 == 3?
- False.
- 6
- Não há garantias de que 1+1+1 == 3 é verdadeiro.
- True. --» Correto

2. Considere que a variável is_ready é do tipo booleano. Qual declaração está correta e é a forma mais elegante de testar se is_ready é verdadeiro?
- if (is_ready == True):
- if (not is_ready = False):
- if (is_ready = True):
- if (is_ready): --» Correto 
- if (not is_ready == False):

3. A linguagem Python permite o uso de funções matemáticas. Porém, não são nativas da linguagem e ficam localizadas em módulos externos. 
Para se usar a função sqrt, por exemplo, é necessário usar o seguinte comando:
- export math
- include <math.h>
- import math --» Correto 
- use math

4. Considere o trecho de comandos abaixo. Qual o número da linha que será responsável pela saída (apresentação do resultado ao usuário) desse código?
```py
texto = "computação"
if len(texto) > 10:
    print ("texto com mais de 10 caracteres")
else:
    print ("texto com 10 ou menos caracteres")
```
- linhas 3 e 5.
- linha 5. --» Correto 
- nem linha 3, nem 5.
- linha 3.

5. A legislação de trânsito do Brasil permite que apenas pessoas com no mínimo 18 anos possam habilitar-se para dirigir. 
Considere que exista uma variável idade e você deverá testar se o usuário pode dirigir ou não e, em seguida, exibir uma mensagem correspondente à sua situação. Todas as opções abaixo dão o resultado correto, porém, qual delas utiliza melhor o recurso do if..else? 
```py
#I: 
if (idade < 18): 
    print ("Não pode tirar carteira de habilitação")
if (idade >= 18):
    print ("Pode tirar a carteira de habilitação")
      
#II: 
if (idade < 18): 
    print ("Não pode tirar carteira de habilitação")
else: 
    print ("Pode tirar a carteira de habilitação")
       
#III: 
if (idade < 18): 
    print (" Não pode tirar carteira de habilitação")
else: 
    if (idade >= 18): 
        print ("Pode tirar a carteira de habilitação")

#IV: 
if (idade < 18): 
    print ("Não pode tirar carteira de habilitação")
else: 
    if (idade == 18): 
        print ("Pode tirar a carteira de habilitação")
    else: 
        if (idade > 18): 
            print ("Pode tirar a carteira de habilitação")
```
- Nenhuma das alternativas
- IV
- I
- II --» Correto 
- III

6. Após executar a atribuição x = 10, qual afirmativa é verdadeira?
- x == 20
- x != 20 --» Correto 
- x != 10
- not(x == 10)

7. Qual(is) dos seguintes comandos é(são) equivalente(s) a x != y?
- not (x == y) --» Correto 
- x > y or x < y --» Correto
- x > y and x < y
- x >= y or x <= y

8. Considere a=0, b = 2 e c = 1. O que será impresso pelos comandos abaixo? (Primeiro ajuste corretamente a indentação.) 
```py
if (a > 0):
    if (b > 0):
        print ("Tudo ok para decolagem!")
    else:
    print ("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0):
        print ("Foguete não tem piloto, mas há outros foguetes disponíveis!")
```
- Foguete não tem piloto, mas há outros foguetes disponíveis! --» Correto 
- Tudo ok para decolagem!
- Tanque principal vazio; voando com combustível reserva!
- nada.