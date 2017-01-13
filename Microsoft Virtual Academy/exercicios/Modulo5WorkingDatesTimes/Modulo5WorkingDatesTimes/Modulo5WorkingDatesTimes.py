import datetime


#Ajudar a determinar quanto tempo alguém saiu para cumprir um prazo

#• Diga-lhes quantos dias eles têm para concluir o projeto
#• Para crédito extra, dê-lhes a resposta como uma combinação de semanas e dias 
#(Dica: você vai precisar de algumas das funções matemáticas do módulo em valores numéricos)

# Variables
strDataLimite = " "
dataLimite = 0
totalDias = 0
dataAtual = datetime.date.today()


# Obter data
strDataLimite = input("Inserir a data limite para o seu projeto (mm/dd/yyyy): ")
dataLimite = datetime.datetime.strptime(strDataLimite,"%d/%m/%Y").date()

##Total em dias
#totalDias = dataLimite - dataAtual

#Diferença em semanas e dias
semanas = int(abs(dataLimite - dataAtual ).days / 7)
dias = abs(dataLimite - dataAtual).days % 7

print("Faltam {0} semanas e {1} dias.".format(semanas, dias))


