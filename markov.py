from sys import argv
from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_string = open(file_path).read()

    return file_string


def make_chains(text_string, key_length):
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

    for i in range(len(list_of_words) - key_length):
        ngram_key = [list_of_words[i]]
        #creating tuple of two words
        for n in range(1, key_length):
            ngram_key.append(list_of_words[i + n])  # add word to key_list
        ngram_key = tuple(ngram_key)  # converts to tuple for key
        value = list_of_words[i + key_length]

        #checking to see if two words are in chains dictionary
        #appending value to the list
        if ngram_key in chains:
            chains[ngram_key].append(value)
        #if not, adding it to chains dictionary and giving it a value of next word as a list
        else:
            chains[ngram_key] = [value]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    key_ngram = choice(chains.keys())  # pick a random key tuple from chains
    num_in_ngram = len(key_ngram)       # number of words in key
 
    # initialize variables
    story = ""
    key_ngram_list = []

    for i in range(0, num_in_ngram):    # first n words in story will be words in tuple key
        story += key_ngram[i] + ' '

    while key_ngram in chains:

        nth_word = choice(chains[key_ngram])     # pick a random word from value list
        story += nth_word + " "

        # make the subsequent tuple key:
        for n in range(1, num_in_ngram):  # add last n-1 words to a list
            key_ngram_list.append(key_ngram[n])
 
        key_ngram_list.append(choice(chains[key_ngram])) # add random choice from value list (in key, value) 
        
        # convert list to tuple for key in dictionary
        key_ngram = tuple(key_ngram_list) 
        # flush key_ngram_list for next iteration
        key_ngram_list = []
    
    return story


# main
input_path = argv[1]
n_in_ngram = int(argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_in_ngram)

# Produce random text
random_text = make_text(chains)

print random_text
