import re
import requests

# https://docs.python.org/3/library/re.html?highlight=re#module-re

string_de_teste = 'O gato é bonito'

#padrao = re.search(r'gata', string_de_teste) # r-> RAW String
#padrao = re.search(r'gato', string_de_teste)

#padrao = re.search(r'gat.', string_de_teste) # . -> qualquer coisa

#padrao = re.search(r'gat\w', string_de_teste) # \w -> [a-zA-Z0-9_]

#padrao = re.search(r'\w\w\w\w', string_de_teste)

'''
if padrao:
    print(padrao.group())
else:
    print('Padrão não encontrado. ')
'''

string_de_teste = 'O gato, a gata, os gatinhos, os gatoes, o gat'

#rfindall = re.findall(r'gat\w', string_de_teste)

#rfindall = re.findall(r'gat\w+', string_de_teste) # + -> 1 ou mais

#rfindall = re.findall(r'gat\w*', string_de_teste) # + -> 0 ou mais

#rfindall = re.findall(r'[gat]+', string_de_teste) # + -> 1 ou mais


'''
if rfindall:
    print(rfindall)
else:
    print('Padrão não encont3rado. ')
'''

#############################
#                           #
#   https://regex101.com/   #
#                           #
#############################

site_text = requests.get('http://lacoxinha.com.br/contato').text

reposta = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', site_text)

if reposta:
    print(reposta)
else:
    print('Padrão não encontrado. ')