from twython import TwythonStreamer
from time import gmtime, strftime
import sys
import json

class CustomStreamer(TwythonStreamer):
   def on_success(self, data):
      if "text" in data:
         print json.dumps(data)

   def on_error(self, error_code, data):    
      print "Error: " + str(error_code), data

#Initialize streamer. For now this will suffice, but it should be more secure.
stream = CustomStreamer("ZEXcWlXy7ZE67waSfmwrA",
                        "z7GvjfmsjbBymaGxtdRwspDInJQODHRKIA8sfRtBTQ",
                  "1329801175-5siUFwJwzTYuYxjgVo7jLaPH2NfSO42J8FltLdR", 
                        "SovYNaBJXeYsxC2uBppdBVymrFlPzXlHP2vTGm0TYVCgE")

args = sys.argv[2:]
search_params = sys.argv[1]
for key in args:
   search_params += (" " + key)

#print "Matching results based on your filters..."
stream.statuses.filter(track=str(search_params))
