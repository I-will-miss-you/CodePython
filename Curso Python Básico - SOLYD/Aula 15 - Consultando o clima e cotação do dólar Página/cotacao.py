######################################
#       api.promasters.net.br        #
######################################

import requests
from json import loads
from datetime import datetime
from time import sleep

while True:
    result = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
    cotacao = loads(result.text)

    print('#### COTAÇÃO - $R ####')
    print('Time: ', datetime.now())
    print('Dolar: ', cotacao['valores']['USD']['valor'])
    print('Euro: ', cotacao['valores']['EUR']['valor'])
    print('BTC: ', cotacao['valores']['BTC']['valor'])
    sleep(5)
    print('\n')