'''
try:
    a = 1200 / 0
except:
    print("Divisão por zero, não da para fazer")
'''

'''
try:
    a = 1200 / 0
    a()
except ZeroDivisionError:
    print('Divisão por zero, não da para fazer')
except NameError:
    print('Função não declarada')
'''

'''
try:
    a = 1200 / 0
except Exception as erro:
    print(f"\033[31mErro:{erro}\033[m ")
'''


from time import sleep
def abre_aqrquivo():
    try:
        arquivo = open('arquivo.txt')
        return True
    except Exception as erro:
        print(f"\033[31mErro:{erro}\033[m ")
        return False


while not abre_aqrquivo():
    print('Tentando abrir arquivo')
    sleep(5)
print('Arquivo aberto')


