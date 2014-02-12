from twython import TwythonStreamer
from time import gmtime, strftime
import sys

class CustomStreamer(TwythonStreamer):
   def on_success(self, data):
      if 'text' in data:
         user = data["user"]
         # Formats output to console. Could be done more neatly.
         print '\033[92m', strftime("%Y-%m-%d %H:%M:%S", gmtime()) +\
               ' \033[95m' + "[" + user["screen_name"] + "] -",\
               data['text'].encode('utf-8')

   def on_error(self, error_code, data):    
      print "Error: " + error_code, data

#Initialize streamer. For now this will suffice, but it should be more secure.
stream = CustomStreamer("APP_TOKEN", 
                        "APP_SECRE",
                        "OAUTH_TOKEN", 
                        "OAUTH_SECRET")

args = sys.argv[2:]
search_params = sys.argv[1]
for key in args:
   search_params += ("," + key)

print "Matching results based on your filters..."
stream.statuses.filter(track=str(search_params))
