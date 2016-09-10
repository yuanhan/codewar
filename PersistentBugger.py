# Persistent Bugger
# 6kyu

'''
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:
For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.
 persistence(4) => 0   # Because 4 is already a one-digit number.
 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit

 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number

'''
def persistence(n):
    result = 0
    while n > 9:
        digit = len(str(n)) # be careful about this. It is previously put outside the while-loop.
        temp = n
        product = 1
        for i in range(digit):
            product = product * (temp // (10 ** (digit-i-1)))
            temp = temp % (10 ** (digit - i - 1))
        n = product 
        result = result + 1
    return result

def persistence2(n, result=0):
    if len(str(n)) == 1:
        return result
    else:
        return persistence(reduce(lambda x, y: int(x) * int(y), str(n), 1), result + 1) # call a function inside a function

