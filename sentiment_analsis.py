import tweepy 
from textblob import TextBlob
import Algorithmia




consumer_Key = "consumer_key"
consumer_secret="consumer_secret"
access_token="access_token"
access_token_secret="access_token_secet"



auth = tweepy.OAuthHandler(consumer_Key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



neither=[]

api = tweepy.API(auth)

public_tweets = api.search('putin')

hard_disl=""

client = Algorithmia.client('sims9xzlf9RkMNblUgjTK51/teM1')
algo = client.algo('nlp/SentimentAnalysis/1.0.3')

for tweet in public_tweets:
	hard_disk=tweet.text
	print(hard_disk)
	neither.append(hard_disk)
	




print(neither[4].upper())

for i in neither:
    input = {"document": i}
    client = Algorithmia.client('sims9xzlf9RkMNblUgjTK51/teM1')
    algo = client.algo('nlp/SentimentAnalysis/1.0.3')
#print algo.pipe(input)
    result = algo.pipe(input)
    print(result.result)