minha_lista = ['Gui', 'João']  # LISTA (list)
minha_tupla = ('Gui', 'João')  # TUPLA (tuple)
meu_dicionario = {'nome': 'Guilherme', 'idade': 27}  # DICIONARIO (dict)
meu_conjunto = {'Gui', 'João', 'Gui', 'Eduardo', 'Ana', 'Zé'}  # CONJUNTO (set)

# INICIALIZAR A ESTRUTURAS VAZIAS
lista = []
tupla = ()
dicionario = dict()
# ou
dicionario = {}
conjunto = set()

'''
# TUPLA
print(minha_tupla)
print(type(minha_tupla))
print(minha_tupla[0])
print(minha_tupla[1])

for nome in minha_tupla:
    print(nome)

#minha_tupla[0] = 'João'
#minha_tupla = ('João', 'Fabricio')
#print(minha_tupla)

if 'Gui' in minha_tupla:
    print('Gui esta na colecao')
if 'Patricia' in minha_tupla:
    print('Gui esta na colecao')
'''

'''
# DICIONARIO
print(meu_dicionario['nome'])
print(meu_dicionario['idade'])
print(len(meu_dicionario))
if 'Guilherme' in meu_dicionario.values():
    print('Guilherme eata no dicionario')

for valores in meu_dicionario.values():
    print(valores)
for valores in meu_dicionario.keys():
    print(valores)

meu_dicionario['nome'] = 'João'
meu_dicionario['endereco'] = 'Av. João das Neves'
meu_dicionario['telefone'] = '123456789'
print(meu_dicionario)

meu_dicionario.clear()
print(meu_dicionario)
'''

'''
#CONJUNTOS
print(meu_conjunto)
meu_conjunto.add('Maria')
meu_conjunto.add('Gui')
print(meu_conjunto)

if 'Gui' in meu_conjunto:
    print('Foi encontrado dentro do conjunto')

print(meu_conjunto.pop())
'''

# Estruturas aninhadas
loucura = [(1, 2), (3, 4), (5, 6), ({'João', 'maria'}, {'gabriel'})]
print(loucura)
