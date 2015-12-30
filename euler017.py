"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-
two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
"""

from collections import Counter
from num2words import num2words
from string import ascii_lowercase as letters

def answer(bound):
    char_counts = Counter()
    for num in xrange(1, bound+1):
        char_counts += Counter(char for char in num2words(num, lang='en_GB'))

    return sum(char_counts[char] for char in letters)

if __name__ == '__main__':
    print answer(1000)
