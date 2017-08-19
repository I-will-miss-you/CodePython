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
from urllib import parse


consumer = oauth2.Consumer(Consumer_Key, Consumer_Secret)
token = oauth2.Token(Access_Token, Access_Token_Secret)
cliente = oauth2.Client(consumer, token)


query = input('Novo Tweet: ')
query_cod = parse.quote(query, safe='')

requisicao = cliente.request(f"https://api.twitter.com/1.1/statuses/update.json?status={query_cod}", method='POST')

twitters = loads(requisicao[1])

print(twitters)
