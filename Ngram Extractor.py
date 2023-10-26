import os
import re
import functions as f

import nltk
from nltk.util import ngrams
from nltk.corpus import wordnet as wn


# Run the code below only when the nltk_data folder doesn't exist to
# downloading the NLTK packages in your system.

# Define the folder name for NLTK data
# folder_name = "nltk_data"
# nltk_data_dir = os.path.join(os.getcwd(), folder_name)
#
# Create the nltk_data directory if it doesn't exist
# if not os.path.exists(nltk_data_dir):
#     os.makedirs(nltk_data_dir)
#
# List of NLTK packages you want to download
# packages = ["punkt", "wordnet", "omw-1.4"]
#
# Download NLTK packages if not already installed in the custom location
# for package in packages:
#     if not os.path.exists(os.path.join(nltk_data_dir, package)):
#         nltk.download(package, download_dir=nltk_data_dir)

# user inputs
version_num = (
    input(
        "\nWhich code version do you want to run ('one' or 'two'): ").strip()
    .lower())
ngram_range = int(input("\nType in max n-gram level number (inclusive): "))
text = input("\nEnter a text: ")

# remove punctuations
cleaned_text = re.sub(r"[^\w\s]", "", text).split(" ")


def main(version_num, ngram_range, cleaned_text, file_name1, file_name2):
    # read in data files &
    # store it in a dictionary
    indexes = f.read_file(file_name1)
    noun_key_dict = f.create_dict(indexes)

    data = f.read_file(file_name2)
    key_def_dict = f.create_dict(data)

    # combine data from dicts
    noun_def_dict = f.rearrange_dicts(noun_key_dict, key_def_dict)

    # iterate loop until number of ngrams_range
    for ngram in range(2, ngram_range + 1):

        print(f"\n{ngram} level n-gram\n")

        # checks version no and then execute the
        # block accordingly
        if version_num == "one":
            for start_idx, end_idx in enumerate(
                    range(ngram, len(cleaned_text) + 1, 1)):

                # concatenate words to form n-grams
                n_gram_phrase = "_".join(cleaned_text[start_idx:end_idx])

                # find the def of a given n-gram in a dictionary
                # if not, then return a blank string
                definition = noun_def_dict.get(n_gram_phrase, '')
                print(n_gram_phrase, definition, sep=", ")

        elif version_num == "two":
            n_grams = ngrams(cleaned_text, ngram)
            words = ["_".join(gram) for gram in n_grams]

            # find word def in a WordNet database
            # using NLTK library
            for word in words:
                definition = f.word_definition(word)
                print(f"{word}, {definition}" if definition else f"{word},")

        else:
            print("Invalid input. Please enter either 'one' or 'two'.")
            return


if __name__ == "__main__":
    main(version_num, ngram_range, cleaned_text, "NounsIndex", "NounsData")
