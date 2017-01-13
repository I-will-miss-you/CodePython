#Calculate the total to charge for an order from an online store in Canada
#�	Ask user what country they are from and their order total
#�	If the user is from Canada, ask which province
#�	If the order is from outside Canada do not charge any taxes
#�	If the order was placed in Canada calculate tax based on the province
#   �	Alberta charge .05% General sales Tax (GST)
#   �	Ontario, New Brunswick, Nova Scotia charge .13% Harmonized sales tax
#   �	All other provinces charge .06% provincial sales tax + .05% GST tax
#�	Tell the user the total with taxes for their order

#Variaveis
pais = " "
zona = " "
valorSemImposto = 0
valorFinal = 0

#Variaveis com as taxas a serem aplicadas
GST = 0.05 # alberta
HST = 0.13 # ontario , new brunswick , nova scotia 
PST = 0.06 # other: PST + GST

#Entrada de valore
pais = input("Pais de origem: ")
if pais.lower() == "canada" :
    zona = input("Provincia: ")

valorSemImposto = float(input("Valor base: "))


# calcular o valor final
if pais.lower() == "canada" :
    if zona.lower() == "alberta":
        valorFinal = valorSemImposto + valorSemImposto * GST
    elif zona.lower() == "ontario" or zona.lower() == "new brunswick" or zona.lower() == "nova scotia" :
        valorFinal = valorSemImposto + valorSemImposto * HST
    else :
        valorFinal = valorSemImposto + valorSemImposto * GST + valorSemImposto * PST
else:
    valorFinal = valorSemImposto

#Returno do resultado
print("Valor a pagar %.2f"%valorFinal)