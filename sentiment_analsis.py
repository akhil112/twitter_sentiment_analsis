import tweepy 
from textblob import TextBlob
import Algorithmia


# #good words in a list
# good_words_list=[]
# good_words_count=0
# words=open('positive-words.txt','r')
# #good_words=words.list(words)
# for i in words:
# 	good_words_list.append(i).
# #good_words_list=good_words.split(" ")


# #bad words in a list
# bad_words_list=[]
# bad_words_count=0
# words1=open('negative-words.txt','r')
# #good_words=words1.list(words)
# for i in words1:
# 	bad_words_list.append(i)

#bad_words_list=bad_words.split(" ")

consumer_Key = "jkAuhNgO3miH5vpbG4VdisWGX"
consumer_secret="j5SQAlEUT11Obas2p7Hl8aMhL8aXELj4OAP4VdXuSUnGOJ2X0K"
access_token="1940806638-tUn9eIukLtyYmypJByAvwVJX8IlY5dnFzug33Go"
access_token_secret="PckPmLyfCCrNQ34eaKH4Ap0eePGjYEyojXmRxwQr3Ot42"

auth = tweepy.OAuthHandler(consumer_Key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


# bad=['hate','asshole','stupid']
# good=['to','the','.']
neither=[]

api = tweepy.API(auth)

public_tweets = api.search('putin')
#public_tweets = api.home_timeline()

#public_tweets=tweepy.Cursor(api.search, q='cricket', geocode="-22.9122,-43.2302,1km").items(10)
hard_disl=""

client = Algorithmia.client('sims9xzlf9RkMNblUgjTK51/teM1')
algo = client.algo('nlp/SentimentAnalysis/1.0.3')

for tweet in public_tweets:
	hard_disk=tweet.text
	print(hard_disk)
	neither.append(hard_disk)
	

	
 #    input = {
 #             hard_disk
 #            }
 #    result = algo.pipe(input)
 #    print(result.result



#   print(tweet.text)
    # hard_disk=tweet.text
    # tweet_split=hard_disk.split(" ")
    # for i in tweet_split:
    # 	if i in good_words_list:
    # 		good_words_count=good_words_count+1
    # 		print("tweet is positive")

    # 	elif i in bad_words_list:
    # 		bad_words_count=bad_words_count+1
    # 		print("tweet is negative")

    # 	else:
    # 	    print("tweet is neutral")


#   analysis = TextBlob(tweet.text)
#   print(analysis.sentiment)
#   print("")


print(neither[4].upper())

for i in neither:
    input = {"document": i}
    client = Algorithmia.client('sims9xzlf9RkMNblUgjTK51/teM1')
    algo = client.algo('nlp/SentimentAnalysis/1.0.3')
#print algo.pipe(input)
    result = algo.pipe(input)
    print(result.result)