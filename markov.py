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
        of first 500 tweets from user timeline.
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

        # Generate string of words from users tweets
        tweet_string = self.generate_twitter_text_string()

        # Create list of words from user tweets
        words = tweet_string.split()
        number_of_words = len(words)

        # Iterate over list and create dictionary of word tuples (i.e. n_grams)
        for index in range(number_of_words - (self.n_gram_size - 1)):
            n_gram = tuple(words[index:(index + self.n_gram_size)])

            try:
                chains[n_gram] = chains.get(n_gram, []) + [words[index + self.n_gram_size]]
            except IndexError:
                chains[n_gram] = chains.get(n_gram, []) + [None]

        return chains

    def make_markov_sentence(self):
        """Returns a random sentence based on dictionary of user markov chains"""

        # Pick random key tuple that starts with a capital letter
        while True:
            phrase = random.choice(self.markov_chains.keys())
            if phrase[0][0].isupper():
                break

        # Initialize the sentence text in as a list starting with the random tuple
        text = list(phrase)

        # Continue to iterate through the dictionary and add to text until you 
        # reach a None value or the end of a sentence, based on punctuation
        while True:
            word_options = self.markov_chains[phrase]
            next_word = random.choice(word_options)

            if next_word is None:
                break

            text.append(next_word)

            if next_word[-1] in '.?!':
                break

            phrase = phrase[1:] + (next_word,)

        # Join the list of text into a string
        text = ' '.join(text)

        return text

    def make_markov_tweet(self):
        """Generates a random tweet."""

        # Make a sentence less than or equal to 140 characters
        while True:
            sentence = self.make_markov_sentence()
            if len(sentence) <= 140:
                break
            else:
                continue

        # Hold the original sentence in variables in case we need to refer to it below
        origin_sentence_words = sentence.split(' ')
        origin_tuple = tuple(origin_sentence_words[-self.n_gram_size:])

        # Create new variables to update and add to original sentence
        words_in_sentence = sentence.split(' ')
        last_group_of_words = tuple(words_in_sentence[-self.n_gram_size:])

        # Initialize number of tries to get our tweet close to 140 characters
        tries = 0

        # Continue to iterate through the dictionary and add to text until you 
        # reach a None value or the end of a sentence, based on punctuation
        # Returns added phrase if under 140 characters
        while tries < 1000:
            word_options = self.markov_chains[last_group_of_words]
            next_word = random.choice(word_options)
            tries += 1

            if next_word is None:
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

        # Otherwise, return original sentence
        return sentence
