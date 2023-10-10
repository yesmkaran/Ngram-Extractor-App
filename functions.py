import nltk
from nltk.util import ngrams
from nltk.corpus import wordnet as wn


def read_file(file_name):
    with open(f'data/{file_name}.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()

    return data


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


def rearrange_dicts(noun_key_dict, key_def_dict):
    noun_def_dict = {}

    for key, value in noun_key_dict.items():
        for v in value:
            try:
                noun_def_dict[key] = key_def_dict[v]
            except KeyError as e:
                continue

    return noun_def_dict


def word_definition(word):
    synsets = wn.synsets(word)

    word_defs = []
    for synset in synsets:
        lemma = synset.lemmas()[0]
        word_def = lemma.synset().definition()
        word_defs.append(word_def)

    return word_defs
