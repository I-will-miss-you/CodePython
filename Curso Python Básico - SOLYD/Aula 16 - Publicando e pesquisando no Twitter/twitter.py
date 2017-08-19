#########################################
#                                       #
#   Twitter Developer Documentation     #
#                                       #
#########################################

Consumer_Key = 'your Consumer Key'
Consumer_Secret = 'your Consumer Secret'

Access_Token = 'your Access Token'
Access_Token_Secret = 'your Access Token Secret'

import oauth2
from json import loads
from pprint import pprint
from urllib import parse


consumer = oauth2.Consumer(Consumer_Key, Consumer_Secret)
token = oauth2.Token(Access_Token, Access_Token_Secret)
cliente = oauth2.Client(consumer, token)


query = input('Pesquisa: ')
query_cod = parse.quote(query, safe='')
requisicao = cliente.request(f"https://api.twitter.com/1.1/search/tweets.json?q={query_cod}&lang=pt")
twitters = loads(requisicao[1])

for twitter in twitters['statuses']:
    print(twitter['user']['screen_name'])
    print(twitter['text'])
    print()



