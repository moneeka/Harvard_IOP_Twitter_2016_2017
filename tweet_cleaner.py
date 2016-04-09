import json
from geopy.geocoders import Nominatim

def tweet_cleaner(coordinateFile, stateTweetsFile, state):
    try:
        # Sets up the geopy portion
        geolocator = Nominatim()
        data = []
        with open(coordinateFile, 'r') as data_file: 

            for line in data_file:
                # converts each line into a json object
                data.append(json.loads(line))
        data_file.close()

        with open(stateTweetsFile, 'w') as clean_data_file:
            for s in data:
                tweet_lat_lon_coordinates = str(s["coordinates"]["coordinates"][1]) + ', '+ str(s["coordinates"]["coordinates"][0])
                location = geolocator.reverse(tweet_lat_lon_coordinates)

                if state in location.address:
                    s["address"] = str(location.address)
                    clean_data_file.write(json.dumps(s))
                    clean_data_file.write("\n")


    except BaseException as e:
        print("Error on_data: %s" % str(e))

    def on_error(self, status):
        print(status)
        return True
