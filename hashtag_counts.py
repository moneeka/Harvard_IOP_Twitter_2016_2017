import cPickle, os

# produces a dictionary of the form:
# { hashtag1: [(date1, count1), (date2, count2), and so on with tuples for each day], hashtag2: [another list of tuples]}

# for every day, pull out the top 20 hashtags and their counts
# for each hashtag, find count for every day in the data (NOTE: this lowercases all hashtags)
hashtags_dict = {}
data_path = os.path.dirname(os.path.abspath(__file__)) + "/TagCounts"
data_files = os.listdir(data_path)
for n in data_files:
    fin = open("TagCounts/"+n, 'r')
    l = cPickle.load(fin)
    # extract the date from the name of the file
    date = n.split('tag')[1].split('.pkl')[0]
    for i in range(0,20):
        # extract hashtag and the count separately (makes all hashtags lower case)
        hashtag = l[i][0].lower()
        count = l[i][1]
        tup = (date, count)
        # add that hashtag to the dict if not already in there, and its count with the date
        if hashtag in hashtags_dict:
            # update the key with an addition to its list of counts
            print date
            values_list = hashtags_dict[hashtag]
            values_list.append(tup)
            hashtags_dict[hashtag] = values_list
        else:
            # add a new key and value, which is a list containing the tuple
            hashtags_dict[hashtag] = [tup]
    fin.close()

print hashtags_dict

# THE FOLLOWING CODE TAKES TOO DAMN LONG
# for j in data_files:
#             # now go back and collect the counts for every single day for this particular hashtag
#             bob = open("TagCounts/"+j, 'r')
#             bob_list = cPickle.load(bob)
#             # search the file for the hashtag:
#             for index, val in enumerate(bob_list):
#                 if (val[0].lower() == hashtag):
#                     # add the date and the count to the dict
#                     count = val[1]
#                     tup = (date, count)
#                     if hashtag in hashtags_dict:
#                         values_list = hashtags_dict[hashtag]
#                         values_list.append(tup)
#                         hashtags_dict[hashtag] = values_list
#                     else:
#                         hashtags_dict[hashtag] = [tup]
#                 else:
#                     # then it had zero mentions on that day, and we need to record that too
#                     tup = (date, 0)
#                     if hashtag in hashtags_dict:
#                         values_list = hashtags_dict[hashtag]
#                         values_list.append(tup)
#                         hashtags_dict[hashtag] = values_list
#                     else:
#                         hashtags_dict[hashtag] = [tup]
#             bob.close()