# IOPTwitter
IOP Steam project

This code is heavily based (read: basically taken from) on this <a href="http://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/">tutorial </a>.
I have deleted my API keys, but left in where they should be in twitter.py. I have also deleted the files that contained any of the data I individually have pulled down from Twitter, since you're not allowed to publish that data by putting it in a public GitHub repo.


How it should work: run the twitter.py file in the command line by typing in: python twitter.py

Then when you have enough data, stop the twitter.py file and then run python tokenise.py to tokenise the code. Then to see the results of the map on your localhost, run python -m SimpleHTTPServer 8888 in the command line.

This should get a local server running on localhost:8000 where you can see the map of the tweets.

Issues with the code as of 11/20/15:
<ol>
<li> Needs a way to combine filtering by both location and content. See the bottom of twitter.py </li>
<li> Need to modify the latitude and longitude for New Hampshire. </li>
<li> Need a way to click on the tweets on the map? </li>
<li> Need to start sentiment analysis. </li>
