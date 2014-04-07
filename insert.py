from cassandra.cluster import Cluster
from time import mktime
from datetime import datetime
import json, time

def convert_to_dt(ts):
   t = time.strptime(ts,'%a %b %d %H:%M:%S +0000 %Y')
   dt = datetime.fromtimestamp(mktime(t))
   return dt

json_data = []

with open('output2.json') as f:
    for line in f:
        json_data.append(json.loads(line))

cluster = Cluster(['127.0.0.1'])

session = cluster.connect('twitter')

for tweet in json_data:
    session.execute("""INSERT INTO tweets (username, tweet_id, text, location, created_at)
	                  VALUES (%s, %s, %s, %s, %s)""", \
                     (tweet['user']['screen_name'], tweet['id_str'], tweet['text'], tweet['user']['location'], convert_to_dt(tweet['created_at'])))
session.shutdown()
cluster.shutdown()
