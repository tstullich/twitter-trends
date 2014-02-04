from twython import TwythonStreamer
from time import gmtime, strftime
import sys

class CustomStreamer(TwythonStreamer):
   def on_success(self, data):
      if 'text' in data:
         print '\033[92m', strftime("%Y-%m-%d %H:%M:%S", gmtime()), \
               '\033[95m', data['text'].encode('utf-8')

   def on_error(self, error_code, data):
      print status_code

stream = CustomStreamer("APP_KEY", 
                        "APP_SECRET",
                        "OAUTH_TOKEN", 
                        "OATH_SECRET")

args = sys.argv[2:]
search_params = sys.argv[1]
for key in args:
   search_params += ","
   search_params += key

print "Matching results based on your filters..."
stream.statuses.filter(track=str(search_params))
