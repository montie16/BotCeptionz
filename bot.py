#will find bot accounts soon

import tweepy, time, sys
from keys import keys

argfile = str(sys.argv[1]) #take in a file
CONSUMER_KEY = 'hMvHrXn5lueJkkK021fsIbmli'
CONSUMER_SECRET = 'bJNKLtg3JcgcqpbDnGoMraDSWGI27H4YTXcsu0tnm9ZA86ZRyn'
ACCESS_KEY = '2887902374-JP4nLlMaaKNGWPbYFvRm0l9KXmLRFuZ37RrPLyT'
ACCESS_SECRET = 'DK5n44aqBK1hK7Kw5WMNWrmN2Oa0RposGWR6kaBPgNzdr'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

twts = api.search(q="Hello World!")     
 
#list of specific strings we want to check for in Tweets
t = ['Hello world!',
    'Hello World!',
    'Hello World!!!',
    'Hello world!!!',
    'Hello, world!',
    'Hello, World!']
 
for s in twts:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Howdy!" % (sn) #Replies Howdy to a set user saying Hello World!
            s = api.update_status(m, s.id)

filename = open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	time.sleep(1800) #tweet every 30 minutes