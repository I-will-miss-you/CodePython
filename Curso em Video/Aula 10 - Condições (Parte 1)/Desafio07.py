# Escreva um programa que pergunte o salário de funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salary = float(input('Salário: '))

new_salary = salary * (1.10 if salary > 1250.0 else 1.15)

print("Novo salário: R$ {:.2f}".format(new_salary))
