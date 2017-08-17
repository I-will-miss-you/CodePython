var_verdade = True #Boolean
var_falso = False

#print(type(var_verdade), type(var_falso))
#print(var_verdade)
#print(var_falso)

############################
# Comparações: == != < > <= >= and or

#a = 2
#b = 20
#if a > b:
#    print(a, 'é maior do que', b)
#else:
#    print(a, 'não é maior do que', b)

#######################
print('Opções:'
      '\n 1 - Escrever Guilerme'
      '\n 2 - Escreve João'
      '\n 3 - Escreve Maria')

opcao = input('Escolha um opção: ')

if opcao == '1':
    print('Guilherme')
elif opcao == '2':
    print('João')
elif opcao == '3':
    print('Maria')
else:
    print('Opção invalida')

############################
idade = 50
if not idade == 50:
    print('Você não tem 50 anos')
else:
    print('Você tem 50 anos')