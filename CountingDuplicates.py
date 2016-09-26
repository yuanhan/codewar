# Counting Duplicates
# https://www.codewars.com/kata/counting-duplicates/python
# 6kyu

'''
Description:

Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters that occur more than once in the given string. The given string can be assumed to contain only digits and uppercase and lowercase alphabets.

Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabbcdeB" -> 2 # 'a' and 'b'
"indivisibility" -> 1 # 'i'
"Indivisibilities" -> 2 # 'i' and 's'
'''
from decimal import *


def duplicate_count(text):
    temp = text.upper()
    count = [temp.count(i) for i in temp]
    result = []
    for i in count:
        if i == 1:
            result.append(0)
        else:
            result.append(Decimal(1) / Decimal(i))
    return round(sum(result))


def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
