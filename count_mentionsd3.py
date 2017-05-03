import os
from datetime import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.font_manager as fm
import json
import mpld3
from mpld3 import plugins
from mpld3.utils import get_id
import collections

#make sure phone number data from Google Drive is in a subdirectory of the
#current directory called "PhoneNumberData" 

def nom_mentions(infile, nominee):
    ctr = 0
    with open(infile, 'r') as data_file:
        for line in data_file:
            try:
                json_line = json.loads(line)
                if nominee in json_line['text']:
                    ctr += 1
            except:
                pass

    return(ctr)

fig, ax = plt.subplots(figsize=(14,5))

data_path = os.chdir("PhoneNumberData")
current = os.getcwd()
files = os.listdir(current)

#make sure number of labels , number of colors, and number of transparencies match
nom_list = ['Trump','Gorsuch','Flynn','Sessions']
color_list = ['#435A8B','#374A72','#2B3A59','#1F2940']
alphas =[1.0,0.75,0.5,0.3]

for nom, color, al in zip(nom_list, color_list, alphas):
    mention_counts = []
    dates = []
    for n in files:
        date_string = n[11:-5]
        dt_string = dt.strptime(date_string, '%Y-%m-%d')
        dates.append(dt_string)
        mention_count = nom_mentions(n, nom)
        mention_counts.append(mention_count)
    ax.plot(dates, mention_counts, color, linewidth=3.0, alpha=al)
 
legend = ax.legend(nom_list, loc='upper right', frameon=False, framealpha=0.0)
data_path = os.chdir("..")

#save to d3 plot
mpld3.save_html(fig, "nom_viz.html")