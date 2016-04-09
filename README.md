# IOPTwitter
Harvard IOP STEAM project

This code is heavily based (read: basically taken from) on this <a href="http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/">tutorial </a>.
I have deleted my API keys, but left in where they should be in twitter.py. I have also deleted the files that contained any of the data I individually have pulled down from Twitter, since you're not allowed to publish that data by putting it in a public GitHub repo.

Things you will need before the instructions below will work for you:
<ol>
<li> Twitter developer account, with API key and tokens. </li>
<li> pip install vincent </li>
<li> pip install tweepy </li>
<li> sudo pip install -U nltk </li>
<li> For NLTK, you will need to follow the on-screen instructions to download the correct copora. </li>
</ol>


How it should work: run the twitter.py file in the command line by typing in: python twitter.py
Assuming your raw data file from twitter.py is called "data.json" and the tweets belong to Florida, run the main method from the command line as follows:

python main.py Florida data.json

This will generate several json files: 
<ol>
	<li><b>coordinatePartition.json</b> contains the geo enabled tweets. It contains the tweets with the correct coordinates from where the user tweeted.</li>
	<li><b>placePartion.json</b> contains the tweets that are not geo enabled. Thus, they only contain coordinates in the "place" object which correspond EITHER to where the user is tweeting from or where they're tweeting about.</li>
	<li><b>state_tweets.json</b> contains the tweets that are confirmed to be in both the state and with proper coordinates. This file contains the tweets that will be mapped on the map.</li>
	<li><b>dictionary.json</b> contains the number of times a candidate is mentioned in each state.</li>
</ol>

