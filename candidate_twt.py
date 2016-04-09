import json

class candidate_rec(object):

    def __init__(self, tweet):
        ts = json.loads(tweet)
        self.text = ts['text']
        self.coords = ts['coordinates']
        self.place = ts['place']

    def get_text(self):
        return self.text

    def get_coords(self):
        return self.coords['coordinates']

    def get_place_name(self):
        return self.place['full_name']

    def get_place_coords(self):
        return self.place['coordinates'][0]