from future import Future
from os import path
import hashlib, requests, string, feedparser, json

# May need to be used in the future in case RSS method does not work out
def parse_html(html_file):
   r.headers
   n = 1
   for line in string.split(html_file, '\n'):
      print n, line
      n += 1

# Routine to count the frequency of words in a sentence
def count_words(dictionary, s):
   w = {}
   for word in string.split(s):
      if word.lower() in w:
         w[word.lower()] += 1
      else:
         w[word.lower()] = 1 

   return w

# Will be run to analyze if new Twitter worker needs to be dispatched
def analyze_feeds(list_of_feeds):
   print "Extracting information..."
   entries = []
   word_count = {}
   for feed in list_of_feeds:
      entries.extend(feed["items"])
      
   for entry in entries:
      if not "VIDEO" in entry["title"]:
         word_count.update(count_words(entry["title"]))
      else:
         del entry
   
   for k in word_count:
      if k == "russia":
         print k, word_count[k]
  

# Take in a list of RSS feeds and request an update
def read_feeds():
   print "Reading some RSS feeds..."
   feed_urls = ["http://feeds.bbci.co.uk/news/world/rss.xml", "http://hosted.ap.org/lineups/TOPHEADS.rss?SITE=AP&SECTION=HOME",
                "http://feeds.reuters.com/Reuters/worldNews", "http://rss.nytimes.com/services/xml/rss/nyt/World.xml"]
   
   future_calls = [Future(feedparser.parse, rss_url) for rss_url in feed_urls]
   feeds = [future_obj() for future_obj in future_calls]

   """Checks cache if a feed needs to be updated 
    This feels super inefficient. Will try to make this better
    Will use different way to cache. Probably through a polling method.
    Keeping this here for now.
    with open('feedhash', 'w+') as f:
      # File needs to be created first time around
      d = {}
      fhash = f.read
      if f.read() == "":
         for feed in feeds:
            d[feed["url"]] = feed["version"]
         json.dump(d, f)

      else:
         print "Cache exists will check for updates."
         f.seek(0)
         d = json.load(f)
         for entry in d:
            print entry
    h = hashlib.sha1(str(d)).hexdigest()
    print h"""
   return feeds

# Start reader here.
f = read_feeds()
analyze_feeds(f)
