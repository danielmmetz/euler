# encoding=utf8
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this
value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from string import ascii_uppercase as letters
import operator

letter_score = {char: index+1 for index, char in enumerate(letters)}
letter_score['"'] = 0


def score_name(name, index):
    return (index+1) * sum(letter_score[char] for char in name)


def answer(names):
    names.sort()
    return sum(score_name(name, index) for index, name in enumerate(names))


if __name__ == '__main__':
    with open('euler022_names.txt', 'r') as f:
        names = f.readlines()

    names = names[0].split(',')
    print answer(names)
