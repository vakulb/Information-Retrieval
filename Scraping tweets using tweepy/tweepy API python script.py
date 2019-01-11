import tweepy
import sys
import jsonpickle

# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler('###############','####################')

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)


searchQuery = 'trump OR obama OR politics OR campaign OR white house OR candidate   -filter:retweets'  # this is what we're searching for
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweets_nyc_politics.json' # We'll store the tweets in a json file.

tweetCount = 0
print("Downloading tweets")
with open(fName, 'a') as f:
        try:
            for new_tweets in  tweepy.Cursor(api.search, q=searchQuery, count=100, geocode="40.7127753,-74.0059728,350km").items(20000):
                f.write(jsonpickle.encode(new_tweets._json, unpicklable=False) +'\n')
            print("Download complete")

        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
