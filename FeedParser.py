import feedparser
import json

f = open('nyt', 'w')

d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
length = len(d['entries'])
for entry in d['entries']:
	article = {'Title': entry['title'], 'PubDate': entry.published}
	json.dump(article, f)
f.close()


f2 = open('wsj', 'w')

d = feedparser.parse('http://www.wsj.com/xml/rss/3_7085.xml')
length = len(d['entries'])
for entry in d['entries']:
	article = {'Title': entry['title'], 'PubDate': entry.published}
	json.dump(article, f2)
f2.close()

f3 = open('breitbart', 'w')

d = feedparser.parse('http://feeds.feedburner.com/breitbart?format=xml')
length = len(d['entries'])
for entry in d['entries']:
	article = {'Title': entry['title'], 'PubDate': entry.published}
	json.dump(article, f3)
f3.close()