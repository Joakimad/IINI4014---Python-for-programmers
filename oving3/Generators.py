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


def myrange_list(start, end):
    res = []
    for num in range(start, end):
        res.append((num, end - num))
    return res


def myrange_gen(start, end):
    for num in range(start, end):
        yield num, end - num


print('LIST: ')
res = [x for x in myrange_list(1, 10)]
print(res)
print(type(res[0]))

print('GEN: ')
res = [x for x in myrange_gen(1, 10)]
print(res)
print(type(res[0]))

# def myrange_list(start,end):
#     list = []
#     # With i as an increasing number in the range of the interval
#     for i in range(0, end - start):
#         # Append a tuple where i is added to start
#         # and subtracted from end-1
#         list.append((start + i, end - 1 - i))
#     return list
#
# def myrange_gen(start,end):
#     # With i as an increasing number in the range of the interval
#     for i in range(0, end - start):
#         # Generate a tuple where i is added to start
#         # and subtracted from end-1
#         yield start + i, end - 1 - i
