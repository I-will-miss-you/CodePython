#################
# r - read
# w - write
# a - append
# r+ - read and write
# b - binary mode

'''
arquivo = open('arquivo.txt', 'w')

#print(arquivo)

for i in range(0, 1000):
    arquivo.write(str(i)+"\n")
'''

'''
arquivo = open('arquivo.txt', 'r')

#print(arquivo.read())

for linha in arquivo:
    print(linha)
'''

arquivo = open('ferro.png', 'rb')
print(arquivo.read())
