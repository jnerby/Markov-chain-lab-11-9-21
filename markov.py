"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()


    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    ind = 0

    words = text_string.split()
    # generate keys of bigrams for dictionary
    for word in words: 
        # check not at last word
        if ind < len(words)-2:
            # generate key from index
            tup = (words[ind], words[ind + 1])
            # if tuple already exists: append next word
            if tup in list(chains.keys()):
                chains[tup].append(words[ind + 2])
            # else (if tuple does not exist), create tuple and create value list w/ next word in it
            else:
                chains[tup] = [words[ind + 2]]
        ind += 1
        
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # get list of all keys
    keys = list(chains.keys())

    last_tup = keys[len(keys)-1]
    # get second word from first key
    key1 = keys[0][1]
            #'you'
    # access first key's value list
    key2_list = chains[keys[0]]
    # get random word from key1's value list
    key2 = choice(key2_list)
            # could or like
    
    # add key1 and key2 to words list
    words.append(key1)
    words.append(key2)

    
    # combine keys to make searchable tuple
    search = (key1, key2)
    
    while search != last_tup:
        # generate random word from value list of search tuple
        random_word = choice(chains[search])

        # append random word to words list
        words.append(random_word)

        # update search tuple
        search = (search[1], random_word)

    words.append(choice(chains[last_tup]))

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print(random_text)
