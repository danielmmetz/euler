# encoding=utf8
"""
The nth term of the sequence of triangle numbers is given by, t_n = n(n+1)/2; so
the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t_10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""

from string import ascii_uppercase as letters


def word_value(word, lookup):
    return sum(lookup[letter] for letter in word)


def extend_tnums(target, nums_arr, nums_set):
    while nums_arr[-1] < target:
        n = len(nums_arr) + 1
        nums_arr.append(n*(n+1)/2)
        nums_set.add(n*(n+1)/2)
    return nums_arr, nums_set


def answer(fname):
    with open(fname, 'r') as f:
        words = f.readlines()[0].split(',')
    words = [word.strip('"') for word in words]

    letter_lookup = {letter: index+1 for index, letter in enumerate(letters)}
    count, tnums_arr, tnums_set = 0, [1], {1}
    for word in words:
        value = word_value(word, letter_lookup)
        tnums_arr, tnums_set = extend_tnums(value, tnums_arr, tnums_set)
        if value in tnums_set:
            count += 1
    return count


if __name__ == '__main__':
    print answer('euler042_words.txt')