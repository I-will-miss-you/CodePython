
#   Taxa de juros
# M = L [i(1 + i)n] / [(1 + i)n - 1]
# M -> pagamento mensal
# L -> montante do empréstimo
# i -> taxa de juro ( i = 0.05)
# n -> número de pagamentos

pagamentoMensal = 0.0
montanteEmprestimo = 0
taxaDeJuro = 0
numeroDePagamentos = 0
duracaoEmprestimoAnos = 0

# Entrada de dados
montanteEmprestimo = float(input("Valor do emprestimo: "))
taxaDeJuro = float(input("Taxa de juros: ")) / 100
duracaoEmprestimoAnos = float(input("Duracao em anos do emprestimo: "))

#Numero de prestações
numeroDePagamentos = duracaoEmprestimoAnos * 12

# Calcular mensalidade
pagamentoMensal = montanteEmprestimo * (taxaDeJuro * (1 + taxaDeJuro) * numeroDePagamentos) / (taxaDeJuro * (1 + taxaDeJuro) * numeroDePagamentos - 1)

# Apresentação do resultado
print("O seu pagamento mensal será: %.2f" %pagamentoMensal)


