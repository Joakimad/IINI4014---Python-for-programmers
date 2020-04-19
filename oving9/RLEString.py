import re


class RLEString:
    # Class takes in a string and has functions for compression and decompression.
    # Uses run length encoding

    def __init__(self, input_string):
        if input_string == '':
            raise Exception('Empty String!')
        elif re.match(r'[a-zA-Z]*$', input_string):
            self.__mystring = input_string
        else:
            raise Exception("String should only contain alphabetic characters!")
        self.__iscompressed = False

    def compress(self):
        # Raise exception if string has already been compressed
        if self.__iscompressed:
            raise Exception("String is already compressed!")

        counter = 0
        current = ''
        compressed_string = []
        # Iterate through string char by char
        for c in self.__mystring:
            # If c matches the current counting char we raise the counter by one
            if c == current:
                counter += 1
            # If c does not match we end the count and add the occurrence into the new string.
            else:
                if current:
                    compressed_occurrence = str(counter) + current
                    compressed_string.append(compressed_occurrence)
                counter = 1
                current = c
        # Add the last occurrence
        compressed_occurrence = str(counter) + current
        compressed_string.append(compressed_occurrence)

        # Updates mystring with compressed value
        self.__mystring = ''.join(compressed_string)

        # Set iscompressed
        self.__iscompressed = True

    def decompress(self):
        # Raise exception if string is not compressed
        if not self.__iscompressed:
            raise Exception("String is not compressed!")

        decompressed_string = []
        # Uses regex to find all occurrences of compression i.e (3A)
        for s in re.findall(r'\d+[A-Za-z]', self.__mystring):
            # Find amount by taking everything but the last symbol, which is the char
            amount = int(s[:-1])
            char = s[-1]
            # Uses the amount to add that char to the decompressed string
            for i in range(amount):
                decompressed_string.append(char)

        # Updates mystring with decompressed value
        self.__mystring = ''.join(decompressed_string)

        # Set iscompressed
        self.__iscompressed = False

    def iscompressed(self):
        # Returns compression value
        return self.__iscompressed

    def __str__(self):
        # Returns mystring value
        return self.__mystring

