# Write a function getfilelist() that takes a pathname as input and returns a list of .txt files thereunder.
# Write a function getwordfreqs() that takes a filename as input and returns a dictionary of words and their frequencies
# Write a function getcommonwords() that takes as input a list of dictionaries and returns a list of of the most
# frequent words common to all dictionaries.

from os import walk, path
from collections import defaultdict, Counter

def getfilelist(pathname):
    txt_files = []
    for root, dirs, files in walk(pathname):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(path.join(root, file))
    return txt_files


def getwordfreqs(filename):
    word_frequency = defaultdict(list)
    count = Counter()
    words = open(filename)
    words.close()


# TEST AREA 51

# paths = getfilelist("./books")
# for i in paths:
#     print(i)

getwordfreqs("books/folder_00/pg27827.txt")

#
# def getcommonwords(dicts):
#     return 0
#
#     dicts = []
#     # Get the list of files
#     for f in getfilelist(sys.argv[1]):
#         # Get word frequencies
#         dicts.append(getwordfreqs(f))
#
#     # Get common words
#     for w in getcommonwords(dicts):
#         print(w)
