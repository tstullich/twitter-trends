from future import Future
import requests, string, feedparser

# May need to be used in the future in case RSS method does not work out
def parse_html(html_file):
   r.headers
   n = 1
   for line in string.split(html_file, '\n'):
      print n, line
      n += 1

# Will be run to analyze if new Twitter worker needs to be dispatched
def analyze_feeds(list_of_feeds):
   print "Extracting information..."
   entries = []
   for feed in list_of_feeds:
      print feed["url"], "(", feed["version"], ")"
      entries.extend(feed["items"])

   #entries = sorted(entries, key=lambda entry: entry["date_parsed"])
   #entries.reverse() 
   for entry in entries:
      print entry["title"]

# Take in a list of RSS feeds and request an update
def read_feeds():
   print "Reading some RSS feeds..."
   feed_urls = ["http://feeds.bbci.co.uk/news/world/rss.xml", "http://hosted.ap.org/lineups/TOPHEADS.rss?SITE=AP&SECTION=HOME",
            "http://feeds.reuters.com/Reuters/worldNews", "http://rss.nytimes.com/services/xml/rss/nyt/World.xml"]
   
   future_calls = [Future(feedparser.parse, rss_url) for rss_url in feed_urls]
   feeds = [future_obj() for future_obj in future_calls] 

   return feeds

f = read_feeds()
analyze_feeds(f)
