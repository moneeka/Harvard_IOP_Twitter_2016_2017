import feedparser
import json
import time

# The sites we want scraped, along with the base name of the file in which the scraping is saved
site_list = [
    ['http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', 'nyt'],
    ['http://www.wsj.com/xml/rss/3_7085.xml', 'wsj'],
    ['http://feeds.feedburner.com/breitbart?format=xml', 'breitbart'],
    ['http://feeds.foxnews.com/foxnews/latest?format=xml', 'fox'],
    ['http://rss.cnn.com/rss/cnn_topstories.rss', 'cnn']
]

# We will set this up to run once every 12 hours
sleep_duration = 60 * 60 * 12

def scrape_site(site_url, out_fname):
    """
    Open a file with a name of the base name passed in and a timestamp, in the sub-directory feed_data. Scrape
    the site, write the file in json format.
    :param site_url: url of the site to be scraped
    :param out_fname: base name of the file that will contain the scraping
    :return: None
    """
    out_name = '-'.join([out_fname, time.strftime('%Y%m%d-%H%M%S')])
    f = open('feed_data/' + '.'.join([out_name, 'txt']), 'w')
    articles = []
    d = feedparser.parse(site_url)
    length = len(d['entries'])
    for entry in d['entries']:
        title = entry['title']
        summary = (entry['summary']).encode('ascii', 'ignore')
        article = {'Title': title, 'Summary': summary}
        try:
            article['Pubdate'] = entry.published
        except:
            article['Pubdate'] = 'No date of publication'

        articles.append(article)
    json.dump(articles, f)
    f.close()

while (True):
    for i in site_list:
        scrape_site(i[0], i[1])
    time.sleep(sleep_duration)
