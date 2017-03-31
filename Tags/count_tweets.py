import os
from datetime import datetime as dt
import matplotlib.pyplot as plt

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

data_path = os.chdir("PhoneNumberData")
current = os.getcwd()
files = os.listdir(current)

tweet_counts = []
dates = []

for n in files:
	date_string = n[11:-5]
	dt_string = dt.strptime(date_string, '%Y-%m-%d')
	dates.append(dt_string)
	tweet_count = file_len(n)
	tweet_counts.append(tweet_count)

plt.plot(dates, tweet_counts, 'k')
plt.show()

