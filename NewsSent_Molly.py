#get a new API key and install aylienapiclient from https://developer.aylien.com/

from aylienapiclient import textapi

client = textapi.Client("17fd47a3", "e04bf98926505adfbb106de51490b9ce")

sentiment = client.Sentiment({'text': 'Donald Trump Business Decisions in 1980s Nearly Led Him to Ruin'})

print sentiment