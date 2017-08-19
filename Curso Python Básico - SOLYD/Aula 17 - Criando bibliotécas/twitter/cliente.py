from twitterClass import Twitter

consumer_Key = 'your Consumer Key'
consumer_Secret = 'your Consumer Secret'

access_Token = 'your Access Token'
access_Token_Secret = 'your Access Token Secret'

twitter = Twitter(consumer_Key, consumer_Secret, access_Token, access_Token_Secret)

# twitter.tweet("Teste da api twitter com o python")


twitters = twitter.search("Python", 'pt')

for twitter in twitters['statuses']:
    print(twitter['user']['screen_name'])
    print(twitter['text'])
    print()
