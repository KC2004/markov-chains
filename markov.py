from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_string = open(file_path).read()

    return file_string


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    list_of_words = text_string.split()

    chains = {}

    for i in range(len(list_of_words) - 2):
        #creating tuple of two words
        bigram_key = (list_of_words[i], list_of_words[i + 1])
        value = list_of_words[i + 2]

        #checking to see if two words are in chains dictionary
        #appending value to the list
        if bigram_key in chains:
            chains[bigram_key].append(value)
        #if not, adding it to chains dictionary and giving it a value of next word as a list
        else:
            chains[bigram_key] = [value]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    key_bigram = choice(chains.keys())  # pick a random key tuple from chains

    story = "%s %s " % (key_bigram[0], key_bigram[1])

    while key_bigram in chains:

        third_word = choice(chains[key_bigram])     # pick a random word from value list

        story += third_word + " "

        key_bigram = (key_bigram[1], third_word.strip())          # pick a random key tuple from chains

    return story


# main
input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
