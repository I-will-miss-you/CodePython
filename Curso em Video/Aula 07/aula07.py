#   +       Adição
#   -       Subtração
#   *       Multiplicação
#   /       Divisão
#   **      Potência
#   //      Divisão Inteira
#   %       Resto da Divisão

# Ordem de Precedência
#   1º      ()
#   2º      **
#   3º      *   /   //  %
#   4º      +   -

# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer {:>20}!'.format(nome))
# print('Prazer em te conhecer {:<20}!'.format(nome))
# print('Prazer em te conhecer {:^20}!'.format(nome))
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

print("Os valor inseridos ", end='')
print("foram: {} e {}".format(n1, n2))

print('{0} + {1} = {2}'.format(n1, n2, n1 + n2))
print('{0} - {1} = {2}'.format(n1, n2, n1 - n2))
print('{0} * {1} = {2}'.format(n1, n2, n1 * n2))
print('{0} / {1} = {2}'.format(n1, n2, n1 / n2))
print('{0} % {1} = {2}'.format(n1, n2, n1 % n2))
print('{0} // {1} = {2}'.format(n1, n2, n1 // n2))
print('{0} ** {1} = {2}'.format(n1, n2, n1 ** n2))
