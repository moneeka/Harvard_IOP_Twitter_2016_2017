# IOPTwitter
IOP Steam project

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

Then when you have enough data, stop the twitter.py file (^C) and then run python tokenise.py to tokenise the json you've just streamed. Then to see the results of the map on your localhost, run python -m SimpleHTTPServer 8888 in the command line.

This should get a local server running on localhost:8000/map.html where you can see the map of the tweets.

Where we are as of 02/10/2016:
<ol>
<li> We have downloaded considerable data for NH in the days leading up to the primary on Tuesday 02/09/16. See Google drive folder.</li>
<li> Monica to write Python script that will use Geopy to filter out non-NH tweets.</li
<li> Need to count the mentions of each candidate's name; Molly has ownership of this stage, which will take the filtered data and count how many times each candidate's name is mentioned.</li>
<li> Goals: Display the data for each candidate on a website, and then develop a predictive model for the primaries on Twitter.</li>

