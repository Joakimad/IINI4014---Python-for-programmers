# We'll write two functions which will be called by the test harness. The first function myrange_list(start,end),
# will build a list of tuples. The first element of the tuple will start at start and increment until
# (but not including) end. The second will simply be the reverse: decrement from (but not including) end to start.
#
# The second function, myrange_gen(start,end), is a generator function that has the same behaviour, but returns an
# iterator instead. This function must not "return", instead it must "yield".
#
# NOTE: your functions must not print anything.
#
# Example usage:
# >>> [x for x in myrange_gen(1,10)]
# [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]
# >>> [x for x in myrange_list(1,10)]
# [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1)]

# def myrange_list(start,end):


def myrange_gen(start, end):
    for i in range(start, end):
        a = i
        b = end-i
        return a, b


res = [x for x in myrange_gen(1, 10)]
print res
