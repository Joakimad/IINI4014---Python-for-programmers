# Write a function getfilelist() that takes a pathname as input and returns a list of .txt files thereunder.
# Write a function getwordfreqs() that takes a filename as input and returns a dictionary of words and their frequencies
# Write a function getcommonwords() that takes as input a list of dictionaries and returns a list of of the most
# frequent words common to all dictionaries.
import string
import re
from collections import Counter
from os import walk, path


def getfilelist(pathname):
    txt_files = []
    for root, dirs, files in walk(pathname):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(path.join(root, file))
    txt_files.sort()
    return txt_files


# def getwordfreqs(filename):
#     # Creates a dictionary with words as keys and frequency as value
#     with open(filename) as txt:
#         return Counter(txt.read().lower().split())


def getwordfreqs(filename):
    with open(filename, encoding="utf8") as file:
        data = file.read().lower()
        res = re.sub("[^a-z0-9]+", " ", data)
        wordfreqs = Counter(res.split())
    return wordfreqs

    # In this final part, you are to write the function getcommonwords() which takes a list of dictionaries and
    # returns a list of words which are common to each dictionary, and within the top 10 words of that dictionary.
    # Put simply, if the dictionary is sorted in descending order, consider only the first 10 entries.


def getcommonwords(dicts):
    most_used_words = []
    for dict in dicts:
        # Find top 10 words
        dict_most_common_used = []
        for e in dict.most_common(10):
            dict_most_common_used.append(e[0])
        most_used_words.append(dict_most_common_used)
        common_words = set.intersection(*[set(list) for list in most_used_words])
    return common_words


# TEST AREA 51
paths = getfilelist("./books")
print(paths)

dicts = []
for filepath in paths:
    dicts.append(getwordfreqs(filepath))

commonwords = getcommonwords(dicts)
print(commonwords)
