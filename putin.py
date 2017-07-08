import Algorithmia

# input = {
#   "document": "I really like Algorithmia!"
# }
# client = Algorithmia.client('sims9xzlf9RkMNblUgjTK51/teM1')
# algo = client.algo('nlp/SentimentAnalysis/1.0.3')
# #print algo.pipe(input)
# result = algo.pipe(input)
# print(result.result)


input = {
  "sentence": "This old product sucks! But after the update it works like a charm!"
  
}
client = Algorithmia.client('sims9xzlf9RkMNblUgjTK51/teM1')
algo = client.algo('nlp/SocialSentimentAnalysis/0.1.4')
result = algo.pipe(input)
print(result.result)