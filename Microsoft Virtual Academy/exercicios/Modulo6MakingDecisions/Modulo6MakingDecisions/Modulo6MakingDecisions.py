#Calcular taxas de envio para um comprador
#� Solicite ao usu�rio que insira o valor da compra total
#� Se o seu total for inferior a $ 50 acrescente $ 10, caso contr�rio o envio � gratuito
#� Informe ao usu�rio o total final, incluindo os custos de remessa, e formate o n�mero para que pare�a um valor monet�rio
#� N�o se esque�a de testar sua solu��o com
#- um valor > 50
#- um valor < 50
#- um valor de exactamente 50

#Variaveis
valorCompra = 0
custoEnvio = 0
custoTotal = 0


#Receber dados
valorCompra = float(input("Valor da compra: "))

#Calculo do valor a pagar
if valorCompra >= 50 :
    custoEnvio = 0
else :
    custoEnvio = 10

custoTotal = valorCompra + custoEnvio

print("Valor final a ser pago: %0.2f Euro" %custoTotal)