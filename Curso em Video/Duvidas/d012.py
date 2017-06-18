print(30 * '-')
print('Calcular salário por hora')
print(30 * '-')

print('Olá, vamos calcular o quanto você receberá por mês ou dia de acordo com as suas horas trabalhadas.')
salario = float(input('Quanto você ganha por hora em R$: '))
opcao1 = int(input('Você deseja fazer o calculo de suas horas trabalhadas por dia ou mês (1- dia 2- mes) ? [1/2]'))

if opcao1 == '1':
    horas_trabalhadas_por_dia = float(input('Informe a quantidade de horas trabalhadas por dia: '))
    salario_por_hora_dia = salario * horas_trabalhadas_por_dia
    print('O valor do seu salario referente a {} dias é: {} '.format(horas_trabalhadas_por_dia, salario_por_hora_dia))

elif opcao1 == '2':
    horas_trabalhadas_por_mes = float(input('Quantas horas você trabalhou no mês? '))
    salario_hora_por_mes = salario * horas_trabalhadas_por_mes
    print('O valor do seu salário referente a {} horas é: {} '.format(horas_trabalhadas_por_mes, salario_hora_por_mes))

else:
    print('Você não informou uma opção válida, por favor, utilize as opções válidas. ')
