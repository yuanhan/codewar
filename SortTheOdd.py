# Sort the Odd
# https://www.codewars.com/kata/sort-the-odd/python
# 6kyu

'''
Description:

You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
'''





def sort_array(source_array):
    result = []
    odd = []
    even = []
    j = 0
    if source_array == []:
        return []
    else :
        for i in range(len(source_array)) :
            if source_array[i] % 2 == 0:
                even.append(i)
            else :
                odd.append(source_array[i])
        odd.sort() # in place change; otherwise use odd = sorted(odd)
        for i in range(len(source_array)):
            if source_array[i] % 2 ==0:
                result.append(source_array[i])
            else :
                result.append(odd[j])
                j +=1
    return result

def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]

