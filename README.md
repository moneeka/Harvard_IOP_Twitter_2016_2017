# IOPTwitter
Harvard IOP STEAM project

The main.py function takes in the state name (eg "Ohio") and the json file of the tweets from Twitter, which has the file name format of "Ohio2016-03-4.json". It then executes the following steps:

<ol>
<li>Tweet_divider.py divides the tweets into coordinates-filled and place-filled tweets, producing files called coordinatePartitition_Ohio_2016_03_04.json and placePartitition_Ohio_2016_03_04.json. </li>
<li>Tweet_cleaner2.py checks that the tweets in coordinatePartition are actually in the state they're supposed to be. It returns a file of tweets which pass this check, called the statefile: tweets_Ohio_2016-03-04.json.</li>
<li>Sort.py then goes through the statefile and counts the mentions and returns a dictionary of candidates and their number of mentions, and also a dictionary of candidates and the percentage of that day's tweets which mentioned them.</li>
</ol>

So you can start the pipeline up by running:
python main.py Florida Florida_2016-03-04.json

Before all this data wrangling happens, there is the code which streams the data from Twitter itself. This is in twitter.py, and is heavily based (read: basically taken from) on this <a href="http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/">tutorial </a>.
I have deleted my API keys, but left in where they should be in twitter.py. I have also deleted the files that contained any of the data I individually have pulled down from Twitter, since you're not allowed to publish that data by putting it in a public GitHub repo.

Things you will need before the instructions for streaming Twitter data will work for you:
<ol>
<li> Twitter developer account, with API key and tokens. </li>
<li> pip install vincent </li>
<li> pip install tweepy </li>
<li> sudo pip install -U nltk </li>
<li> For NLTK, you will need to follow the on-screen instructions to download the correct copora. </li>
</ol>


How it should work: run the twitter.py file in the command line by typing in: python twitter.py
