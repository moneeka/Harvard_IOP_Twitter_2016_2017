from nltk.tokenize import word_tokenize
import json
import re
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
from nltk import bigrams
import vincent

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

# regular expressions variable; capturing particulr patterns
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

# re.VERBOSE ignores spaces, re.IGNORECASE ignores case
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

# remove stopwords
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', '...']

# the below should process the data
with open('tweets.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        with open('processedtweets.json', 'a') as f:
            f.write(str(tokens))

with open('tweets.json', 'r') as f:
    # count_all = Counter()
    # for line in f:
    #     tweet = json.loads(line)
    #     # Create a list with all the terms
    #     terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
    #     # Update the counter
    #     count_all.update(terms_stop)
    # # Print the first 5 most frequent words
    # print(count_all.most_common(5))
    # # Count hashtags only
    # count_hash = Counter()
    # terms_hash = [term for term in preprocess(tweet['text'])
    #               if term.startswith('#')]
    # print(terms_hash)
    # Count terms only (no hashtags, no mentions)
    count_terms_only = Counter()
    for line in f:
        tweet = json.loads(line)
        terms_only = [term for term in preprocess(tweet['text'])
                  if term not in stop and
                  not term.startswith(('#', '@'))]
        count_terms_only.update(terms_only)
                  # mind the ((double brackets))
                  # startswith() takes a tuple (not a list) if
                  # we pass a list of inputs

# plotting the data
word_freq = count_terms_only.most_common(10)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('nothing.json')

# getting coordinates data from tweets
with open('tweets.json', 'r') as f:
    geo_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for line in f:
        tweet = json.loads(line)
        if tweet['coordinates']:
            geo_json_feature = {
                "type": "Feature",
                "geometry": tweet['coordinates'],
                "properties": {
                    "text": tweet['text'],
                    "created_at": tweet['created_at']
                }
            }
            geo_data['features'].append(geo_json_feature)

# Save geo data
with open('geo_data.json', 'w') as fout:
    fout.write(json.dumps(geo_data, indent=4))
