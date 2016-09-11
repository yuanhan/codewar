# WeIrD StRiNg CaSe
# 6kyu
# https://www.codewars.com/kata/weird-string-case/python

'''
Description:

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:

to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
'''

def to_weird_case(string):
    temp = string.title()
    result = ''
    for i in range(len(string)):
        if temp[i].islower() and result[i-1].islower(): # used to be temp[i-1]
            result = result + temp[i].upper()
        else: 
            result = result + temp[i]
    return result



def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower())) # for each word
    
def to_weird_case2(string):
    return " ".join(to_weird_case_word(str) for str in string.split()) # split into words
