import requests, string, feedparser

def parse_html(html_file):
   r.headers
   n = 1
   for line in string.split(html_file, '\n'):
      print n, line
      n += 1

def read_feeds():
   bbc_feed_url = "http://feeds.bbci.co.uk/news/world/rss.xml"
   feed = feedparser.parse(bbc_feed_url)
   if feed["bozo"] == 1:
      print "This is bozo"
   print feed["url"]
   for entry in feed["items"]:
      print entry["title"]
   print "done"

read_feeds()
