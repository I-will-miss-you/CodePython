# Depurador

1. Sobre as formas de execução dentro do depurador, é certo afirmar que: (assinale todas as alternativas CORRETAS)
- Todas as demais alternativas estão erradas
- Go: executa o programa inteiro --» Correto 
- OVER: executa uma linha inteira e se nela tiver uma chamada de função, ela é executada por completo, 
de uma só vez, sem mostrar o passo a passo dentro dela --» Correto
- STEP: executa uma linha inteira e se nela tiver uma chamada de função, ele entra na função e executa passo a passo --» Correto 
- Não é possível mostrar a execução passo a passo de uma função

2. O quê acontece se eu não selecionar a opção “source” do depurador?
- O depurador não dará novas opções de fontes de dados
- O depurador não irá executar
- O depurador não mostrará os valores das variáveis durante a execução do código
- O depurador não marcará dentro do código fonte a linha que está sendo executada --» Correto 

3. O comando print é uma função.
- Se eu estiver executando a linha que chama essa função, como por exemplo print (“teste”), qual o botão que deverá ser acionado no depurador para entrar nessa função e mostrar passo a passo sua execução?
- Step --» Correto 
- Go
- Quit
- Out
- Over

4. Analise o programa abaixo e assinale as afirmações CORRETAS:
```py
def soma(num1, num2, num3):
    return num1 + num2 + num3

def main():
    n1 = float(input("Primeiro número = "))
    n2 = float(input("Segundo número = "))
    n3 = float(input("Terceiro número = "))
    print (soma(n1, n2, n3))

main()
```
- Todas as alternativas estão INCORRETAS
- As variáveis num1, num2 e num3 só aparecerão no depurador quando a função soma estiver sendo executada --» Correto 
- O programa começará a ser executado pela função soma
- O programa começará a ser executado pela função main --» Correto 
- As variáveis n1, n2 e n3 são globais, ou seja, aparecerão no depurador independente de qual função estará sendo executada
- Esse programa não será executado porque a função soma está sendo chamada dentro de um print. Dará erro de sintaxe
