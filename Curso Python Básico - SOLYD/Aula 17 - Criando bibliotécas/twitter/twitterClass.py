import oauth2
from urllib import parse
from json import loads


class Twitter:
    def __init__(self, consumer_Key, consumer_Secret, access_Token, access_Token_Secret):
        self.cliente = self.conexao(consumer_Key, consumer_Secret, access_Token, access_Token_Secret)

    def conexao(self, consumer_Key, consumer_Secret, access_Token, access_Token_Secret):
        consumer = oauth2.Consumer(consumer_Key, consumer_Secret)
        token = oauth2.Token(access_Token, access_Token_Secret)
        cliente = oauth2.Client(consumer, token)
        return cliente

    def tweet(self, novo_tweet):
        query_cod = parse.quote(novo_tweet, safe='')
        requisicao = self.cliente.request(f"https://api.twitter.com/1.1/statuses/update.json?status={query_cod}",
                                          method='POST')
        return loads(requisicao[1])

    def search(self, query, lang):
        query_cod = parse.quote(query, safe='')
        requisicao = self.cliente.request(f"https://api.twitter.com/1.1/search/tweets.json?q={query_cod}&lang={lang}")
        return loads(requisicao[1])


