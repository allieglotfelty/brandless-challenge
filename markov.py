import random

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
    number_of_words = len(words)
    for index in range(number_of_words - (n - 1)):
        n_gram = tuple(words[index:index + n])

        try:
            chains[n_gram] = chains.get(n_gram, []) + [words[index + n]]
        except IndexError:
            chains[n_gram] = chains.get(n_gram, []) + [None]

    return chains


def make_n_gram_text(chains, cap_at_sentence=False):
    """Takes a dictionary of markov chains and returns a random text"""

    while True:
        phrase = random.choice(chains.keys())
        if phrase[0][0].isupper():
            break
    # phrase = random.choice(chains.keys())
    text = list(phrase)

    while True:
        word_options = chains[phrase]
        next_word = random.choice(word_options)

        if not next_word:
            break
        text.append(next_word)
        if cap_at_sentence:
            if next_word[-1] in '.?!':
                break
        phrase = phrase[1:] + (next_word,)

    text = " ".join(text)

    return text
