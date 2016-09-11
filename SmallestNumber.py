# Find the smallest integer in the array
# 7kyu
# https://www.codewars.com/kata/find-the-smallest-integer-in-the-array/python

'''
Description:

Find the smallest integer in the array.

Given an array of integers your solution should find the smallest integer. For example:
Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345

You can assume, for the purpose of this kata, that the supplied array will not be empty.

'''

def findSmallestInt(arr):
    small = arr[0]
    for i in arr:
        if i < small:
            small = i
    return small

def findSmallestInt2(arr):
    return reduce(lambda x,y: x if x<y else y, arr)

def findSmallestInt3(arr):
    return min(arr)
