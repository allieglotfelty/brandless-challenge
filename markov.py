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

    text = ' '.join(text)

    return text

def make_a_markov_phrase(chains, char_length=140):
    """Generates a random phrase of given character length (default is 140).
    """

    while True:
        sentence = make_n_gram_text(chains, cap_at_sentence=True)
        if len(sentence) <= char_length:
            break
        else:
            continue

    origin_sentence_words = sentence.split(' ')
    origin_tuple = tuple(origin_sentence_words[-2:])
    tries = 0

    words_in_sentence = sentence.split(' ')
    last_two_words = tuple(words_in_sentence[-2:])

    while tries < 200:
        word_options = chains[last_two_words]
        next_word = random.choice(word_options)
        tries += 1

        if not next_word:
            break
        words_in_sentence.append(next_word)

        if next_word[-1] in '.?!':
            phrase = ' '.join(words_in_sentence)
            if len(phrase) <= char_length:
                return phrase
            else:
                last_two_words = origin_tuple
                words_in_sentence = origin_sentence_words
                continue
        last_two_words = last_two_words[1:] + (next_word,)

    return sentence
    
    # phrase = ''
    # tries = 0

    # while tries < 200:
    #     sentence = make_n_gram_text(chains, cap_at_sentence=True)
    #     tries += 1
    #     if len(sentence) <= char_length:
    #         phrase += sentence
    #         char_length = char_length - len(sentence) - 1
    #         if char_length == 0:
    #             break
    #     else:
    #         continue

    # return phrase.strip()
