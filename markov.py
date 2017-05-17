# Markov Class

def make_n_gram_chains(tweet_string, n):
    """Takes input as a string and n as the length of the n-gram and
    returns a dictionary of markov chains.

    A chain will be a key that contains a tuple of (word1, word2,..., wordn) 
    and the values will be a list of words that follow those n words in the
    input string.
    """

    chains = {}

    words = tweet_string.split()
    string_length = len(words)
    for index in range(string_length - (n - 1)):
        n_gram = tuple(words[index:index + n])

        try:
            chains[n_gram] = chains.get(n_gram, []) + [words[index + n]]
        except IndexError:
            chains[n_gram] = chains.get(n_gram, []) + [None]

    return chains
