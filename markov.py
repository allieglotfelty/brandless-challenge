import random
import os
import tweepy


class Markov():
    """Markov class"""

    def __init__(self, twitter_handle, n_gram_size=2):
        """Initialize instance of Markov class with Twitter handle, n_gram size,
        and dictionary of n_gram chains.
        """

        self.twitter_handle = twitter_handle
        self.n_gram_size = n_gram_size
        self.markov_chains = self.make_n_gram_chains()

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Markov Twitter handle: %s n_gram_size: %s>" % (self.twitter_handle,
                                                                self.n_gram_size
                                                                )

    def generate_twitter_text_string(self):
        """Access the Twitter API using authentication and generate string
        of first 500 tweets from user
        """

        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token_key = os.environ['TWITTER_ACCESS_TOKEN']
        access_token_secret = os.environ['TWITTER_TOKEN_SECRET']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)

        api = tweepy.API(auth)

        tweets_from_handle = api.user_timeline(screen_name=self.twitter_handle,
                                               count=500)
        tweets_for_markov = ''
        for tweet in tweets_from_handle:
            tweets_for_markov += tweet.text + " "

        tweets_for_markov = tweets_for_markov.encode('ascii', 'ignore')

        return tweets_for_markov

    def make_n_gram_chains(self):
        """Returns a dictionary of markov chains based on the class Twitter
        handle and n_gram size.

        A chain will be a key that contains a tuple of (word1, word2,..., wordn)
        and the values will be a list of words that follow those n words in the
        tweet text string.
        """

        chains = {}

        tweet_string = self.generate_twitter_text_string()
        words = tweet_string.split()
        number_of_words = len(words)

        for index in range(number_of_words - (self.n_gram_size - 1)):
            n_gram = tuple(words[index:index + self.n_gram_size])

            try:
                chains[n_gram] = chains.get(n_gram, []) + [words[index + self.n_gram_size]]
            except IndexError:
                chains[n_gram] = chains.get(n_gram, []) + [None]

        return chains

    def make_markov_sentence(self):
        """Returns a random sentence based on dictionary of user markov chains"""

        while True:
            phrase = random.choice(self.markov_chains.keys())
            if phrase[0][0].isupper():
                break

        text = list(phrase)

        while True:
            word_options = self.markov_chains[phrase]
            next_word = random.choice(word_options)

            if not next_word:
                break

            text.append(next_word)

            if next_word[-1] in '.?!':
                break

            phrase = phrase[1:] + (next_word,)

        text = ' '.join(text)

        return text

    def make_markov_tweet(self):
        """Generates a random tweet."""

        while True:
            sentence = self.make_markov_sentence()
            if len(sentence) <= 140:
                break
            else:
                continue

        origin_sentence_words = sentence.split(' ')
        origin_tuple = tuple(origin_sentence_words[-self.n_gram_size:])

        words_in_sentence = sentence.split(' ')
        last_group_of_words = tuple(words_in_sentence[-self.n_gram_size:])
        tries = 0

        while tries < 1000:
            word_options = self.markov_chains[last_group_of_words]
            next_word = random.choice(word_options)
            tries += 1

            if not next_word:
                break
            words_in_sentence.append(next_word)

            if next_word[-1] in '.?!':
                phrase = ' '.join(words_in_sentence)
                if len(phrase) <= 140:
                    return phrase
                else:
                    last_group_of_words = origin_tuple
                    words_in_sentence = origin_sentence_words
                    continue
            last_group_of_words = last_group_of_words[1:] + (next_word,)

        return sentence
