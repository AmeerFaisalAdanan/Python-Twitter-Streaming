import config
import tweepy

consumer_key = config.CONSUMER_KEY
consumer_secret = config.CONSUMER_SECRET
access_token = config.ACCESS_TOKEN
access_secret = config.ACCESS_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)