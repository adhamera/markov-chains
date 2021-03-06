"""Generate Markov text from text files."""

from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_path = open('green-eggs.txt').read()

    for line in file_path:
        line = line.rstrip()
        


    return  file_path #'Contents of your file as one long string'


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

    # your code goes here
    chains = {}
    words = text_string.split()
    list_values = []

    #tuple_saved = tuple()
    for i in range(0, len(words)-2):
        tuple_saved = (words[i], words[i+1]) #gives us the key
        #chains[tuple_saved] = words[i+2] #assign dictionary key to value
        if tuple_saved in chains:
            list_values.append(words[i+2])
        else:
            list_values = []
    for key, value in chains.items(): #to access the value associated with each tuple       
        print(f'{key}: {value}') #print the values in the key
   
    print(chains)
    return chains
################################################
#     input = "would you eat would you like"
#     chains = {
#         key: ("would", "you"), value: ["eat", "like"]
#         key: ("you", "eat"), value: ["would"]
#     }
#  key_tuple = ("would", "you")
#  chains[key_tuple] = ["eat"]
#  chains[key_tuple].append(words[i+2])

#################################################
def make_text(chains):
    """Return text from chains."""
#For every time through the list:
#1. Check to see if anything is currently in  chains[tuple_saved] - if not, set the value to an empty list---- if key not in chains[tuple_saved]: 
#2. Add the new word to chains[tuple_saved]----- chains[tuple_saved].append(words[i+2])

    # value_list = []

    # for item in chains[tuple_saved]:
            

    #print(words_list)


    #return ' '.join(words_list)


# input_path = 'green-eggs.txt'

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
