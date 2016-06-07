# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    # raise NotImplementedError
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    # raise NotImplementedError
    words.sort()
    while words[-1][0] == 'x':
        last = words.pop()
        words.insert(0, last)
    return words


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    # raise NotImplementedError
    last_list = sorted(tuples, key=lambda x: x[-1])
    return last_list


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    # raise NotImplementedError
    non_adj = []
    for i in range(len(nums)):
        if i == 0:
            non_adj.append(nums[0])
        elif nums[i] != nums[i-1]:
            non_adj.append(nums[i])
    return non_adj


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """
    # raise NotImplementedError
    list1 += list2
    list1.sort()
    return list1
    
#   TRIED OTHER METHODS 

# def linear_merge(list1, list2):
#     for i in range(max(len(list1), len(list2))):
#         while len(list2) > 0:
#             if list1[i] > list2[0]:
#                 print list1[i], list2[0], list1[i] < list2[0]
#                 list1.insert(i, list2.pop())
#     return list1

# def linear_merge(list1, list2):
#     x = 0
#     for i in range(min(len(list1), len(list2))):
#         print i, range(min(len(list1), len(list2)))
#         while list1[x] < list2[0]: # for >
#             print list1[x], list2[0], list1[x] > list2[i]
#             list1.insert(x, list2[i])
#             print list1
#             x += 1
#     return list1
