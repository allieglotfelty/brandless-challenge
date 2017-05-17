import os
import tweepy


def connect_to_twitter(twitter_handle):
    """Access the Twitter API using authentication"""

    consumer_key = os.environ['TWITTER_CONSUMER_KEY']
    consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
    access_token_key = os.environ['TWITTER_ACCESS_TOKEN']
    access_token_secret = os.environ['TWITTER_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    tweets_from_handle = api.user_timeline(screen_name=twitter_handle, count=5)
    tweets_for_markov = ''
    for tweet in tweets_from_handle:
        tweets_for_markov += tweet.text + " "

    tweets_for_markov = tweets_for_markov.encode('ascii', 'ignore')
    
    return tweets_for_markov

print connect_to_twitter("@realdonaldtrump")
