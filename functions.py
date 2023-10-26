import nltk
from nltk.util import ngrams
from nltk.corpus import wordnet as wn


def read_file(file_name):
    with open(f'data/{file_name}.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()

    return data


# creates a dictionary from a list of lines where each line
# contains key-value pairs.
def create_dict(data):
    data_dict = {}
    for line in data:
        line_parts = line.split('|')
        # Remove newline character from the key
        key = line_parts[0].rstrip('\n')

        # Remove newline character from values
        values = [value.rstrip('\n') for value in line_parts[1].split(',')]
        data_dict[key] = values

    return data_dict


# rearranges data from two dictionaries
# to create a new dictionary.
def rearrange_dicts(noun_key_dict, key_def_dict):
    noun_def_dict = {}

    for key, value in noun_key_dict.items():
        for v in value:
            try:
                # associate the noun (key) with its definition
                # from 'key_def_dict'.
                noun_def_dict[key] = key_def_dict[v]
            except KeyError as e:
                # key is not found in 'key_def_dict',
                # continue to the next value.
                continue

    return noun_def_dict


# retrieves the definitions of a word
# using WordNet.
def word_definition(word):
    # Get a list of synsets for the input 'word' from WordNet.
    synsets = wn.synsets(word)

    word_defs = []
    for synset in synsets:
        # Get the first lemma (word form) of the synset
        lemma = synset.lemmas()[0]

        # Retrieve the definition associated with the synset
        # and add it to the 'word_defs' list.
        word_def = lemma.synset().definition()
        word_defs.append(word_def)

    return word_defs
