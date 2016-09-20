# power of 2
# 8kyu
# http://www.codewars.com/kata/powers-of-2/python

'''
Description:

Write a function powersOfTwo which will return list of all powers of 2 from 0 to n (where n is an exponent).

E.g:

n = 0 -> 2^0 -> [1]

n = 1 -> 2^0, 2^1 -> [1,2]

n = 2 -> 2^0, 2^1, 2^2 -> [1,2,4]

'''

# my solution


def powers_of_two(n):
    temp = []
    for i in range(n + 1):
        temp[len(temp):] = [2**i]
    return temp


def powers_of_two(n):
    return [2**x for x in range(n + 1)]


def powers_of_two(n):
    return [1 << x for x in range(n + 1)]


def powers_of_two(n): return [2 ** i for i in range(n + 1)]
