import requests  # Beautiful Soup 4 BS4 pip install bs4

'''
texto = None
try:
    #requisicao = requests.get('https://g1.com.br')
    requisicao = requests.get('http://g1.com.br')
    texto = requisicao.text
except Exception as e:
    print(f"\033[31mRequisição deu erro: {e}\033[m ")

#print(requisicao)
#print(type(requisicao))

#print(requisicao.status_code)

print(texto)
'''


#######################################
# USAR O site http://www.putsreq.com/ #
#######################################

'''
texto = None
try:
    requisicao = requests.post('http://www.putsreq.com/Q6niE4NeDHW8l8dWIuTB')
    texto = requisicao.text
except Exception as e:
    print(f'\033[31mErro: {e}\033[m')

print(texto)
'''

cabecalho = {'User-agent': 'Windows 12',
             'Referer': 'https://google.com'
             }

meus_cookies = {'Ultima-visita':'10-10-2020'}

dados = {'username':'guigui',
         'password':'guigui123'}

texto = None
try:
    requisicao = requests.post('http://www.putsreq.com/Q6niE4NeDHW8l8dWIuTB',
                               headers=cabecalho,
                               cookies=meus_cookies,
                               data=dados)
    texto = requisicao.text
except Exception as e:
    print(f'\033[31mErro: {e}\033[m')

print(texto)
