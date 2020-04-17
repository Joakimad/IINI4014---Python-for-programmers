# Write a function getfilelist() that takes a pathname as input and returns a list of .txt files thereunder.
# Write a function getwordfreqs() that takes a filename as input and returns a dictionary of words and their frequencies
# Write a function getcommonwords() that takes as input a list of dictionaries and returns a list of of the most
# frequent words common to all dictionaries.
import string
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
    wordfreqs = Counter()
    remove_punctuations = str.maketrans('', '', string.punctuation)
    with open(filename, encoding="utf8") as file:
        for line in file:
            whitelist = string.ascii_letters + string.digits + ' '
            line = ''.join(c for c in line if c in whitelist)
            #line = line.translate(remove_punctuations)
            wordfreqs.update(line.lower().split())
    return wordfreqs

    # In this final part, you are to write the function getcommonwords() which takes a list of dictionaries and
    # returns a list of words which are common to each dictionary, and within the top 10 words of that dictionary.
    # Put simply, if the dictionary is sorted in descending order, consider only the first 10 entries.


def getcommonwords(dicts):
    commonwords = []
    for dict in dicts:
        # Find top 10 words
        dict_most_common_used = []
        for e in dict.most_common(10):
            dict_most_common_used.append(e[0])
        commonwords.append(dict_most_common_used)
    return commonwords


# TEST AREA 51
paths = getfilelist("./books")
print(paths)
dicts = []
for filepath in paths:
    dicts.append(getwordfreqs(filepath))

print(len(dicts[0]))
print(dicts[0])

# for dict in dicts:
#    print(len(dict))

# print(getwordfreqs("testfile.txt"))

# c1 = Counter({'big': 5, 'small': 5, 'tiny': 5, 'little': 3, 'huge': 3, 'normal': 1})
# c2 = Counter({'small': 7, 'little': 5, 'tiny': 4, 'big': 1, 'normal': 1, 'huge': 1})
# c3 = Counter({'small': 10, 'big': 8, 'tiny': 9, 'little': 7, 'huge': 7, 'normal': 1})
#
# c1 = Counter({'c1-1': 5, 'c1-2': 4, 'c1-3': 3, 'c1-4': 2})
# c2 = Counter({'c2-4': 2, 'c2-3': 3, 'c2-2': 4, 'c2-1': 5})
# c3 = Counter({'c3-3': 3, 'c3-2': 4, 'c3-1': 5, 'c3-4': 2})
# default_dicts = [c1, c2, c3]
#
# c4 = Counter({'small': 3, 'big': 8, 'tiny': 9, 'little': 7, 'huge': 7, 'normal': 1})
# mostcommon = c4.most_common(3)
#
# a = getcommonwords(default_dicts)
# print(a)
