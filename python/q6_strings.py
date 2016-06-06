# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    # raise NotImplementedError
    if count < 10:
        return 'Number of donuts: %s' % count
    else:
        return 'Number of donuts: many'


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    # raise NotImplementedError
    if len(s) > 2:
        result = s[:2] + s[-2:]
        return result
    else:
        return ""


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    # raise NotImplementedError
    length = len(s)
    for i in range(length):
        if i != 0:
            if s[i] == first_char:
                next_char = '*'
            else:
                next_char = s[i]
            new_word += next_char
        else:
            first_char = s[i]
            new_word = s[i]
    return new_word


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    # raise NotImplementedError
    s1_chars = a[:2]
    s2_chars = b[:2]
    s1 = s2_chars + a[2:]
    s2 = s1_chars + b[2:]
    return s1 + " " + s2


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    # raise NotImplementedError
    if len(s) >= 3:
        if s[len(s)-3:] == 'ing':
            ending = 'ly'
        else:
            ending = 'ing'
        new_word = s + ending
        return new_word
    else:
        return s


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    # raise NotImplementedError
    try:
        result = s
        if s.index('not') < s.index('bad'):
            full_sub = s[s.find('not'):s.find('bad')+3]
            result = s.replace(full_sub, 'good')
        return result
    except ValueError:
        return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    # raise NotImplementedError
    from math import ceil
    a_front = a[:int(ceil(len(a)/2.0))]
    a_back = a[int(ceil(len(a)/2.0)):]
    b_front = b[:int(ceil(len(b)/2.0))]
    b_back = b[int(ceil(len(b)/2.0)):]
    result = a_front + b_front + a_back + b_back
    return result
