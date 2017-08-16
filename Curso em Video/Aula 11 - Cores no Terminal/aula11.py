'''
    SYTLE       |       TEXT        |       BACK
 0 - None       | 30 - Branco       | 40 - Branco
 1 - Bold       | 31 - Vermelho     | 41 - Vermelho
 4 - Underline  | 32 - Verde        | 42 - Verde
 7 - Negative   | 33 - Amarelo      | 43 - Amarelo
                | 34 - Azul         | 44 - Azul
                | 35 - Roxo         | 45 - Roxo
                | 36 - cyan         | 46 - cyan
                | 37 - cinza        | 47 - cinza
'''

''' 
print('\033[0;30;41m Teste \033[m\n')
print('\033[4;33;44m Teste \033[m\n')
print('\033[1;35;43m Teste \033[m\n')
print('\033[30;42m Teste \033[m\n')
print('\033[m Teste\n')
print('\033[7;30m Teste \033[m\n')
'''

print('\033[7;30mOlá, mundo!\033[m')

a = 3
b = 5

print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Guanabara'
c_red = '\033[31m'
c_reset = '\033[m'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(c_red, nome, c_reset))


cores = {
    'limpa': '\033[m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'preto_branco': '\033[7;30m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['preto_branco'], nome, cores['limpa']))
