import nltk
import tweetstore
from collections import Counter

tweets = []
for (words, sentiment) in tweetstore.pos_tweets + tweetstore.neg_tweets:
	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	tweets.append((words_filtered, sentiment))

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
      all_words.extend(words)
    return all_words

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

word_features = get_word_features(get_words_in_tweets(tweets))


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def classify_tweet(tweet):
    return \
        classifier.classify(extract_features(nltk.word_tokenize(tweet)))

training_set = nltk.classify.apply_features(extract_features, tweets)

classifier = nltk.NaiveBayesClassifier.train(training_set)

test_tweets = tweetstore.test_pos + tweetstore.test_neg
total = accuracy = float(len(test_tweets))

for tweet in test_tweets:
    if classify_tweet(tweet[0]) != tweet[1]:
        accuracy -= 1

print('Total accuracy: %f%% (%d/20).' % (accuracy / total * 100, accuracy))
