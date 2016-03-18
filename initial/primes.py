# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
 
import datetime

# Write a Python function to print out the numbers from 1 to 50. If the function encounters a prime number, it should print out ‘PRIME’ instead of the number. 

def print_primes():
    def prime(x):
        for i in range(2, x/2+1):
            if x % i == 0: 
                return False
        return True
    for i in range(1,51): 
        if (prime(i)):
            print "PRIME"
        else:
            print i

print_primes()

# How would you write a function to compute the squares of numbers from 1 to 1 Billion inclusive in Python?

# Long signed integer type. Capable of containing at least the [−2147483647, +2147483647] range;[3][4] thus, it is at least 32 bits in size.

# https://docs.python.org/2/library/array.html
# array — Efficient arrays of numeric values
# 'L'	unsigned long	long	4

# 4 bytes - 32 bits 2**32 = 4294967296 (4.2 billion - big enough for the number 1 billion, but not its square!)

# >>> 1000000000**2
# 1000000000000000000    # a billion squared
# >>> 2**64
# 1.84467440737e+19      # 20 digits?
# 18446744073709551616L  # unsigned long long? 2^64
# (what does the 'L' mean?) - automatically converted to unsigned long and unlimited?

# >>> sys.maxsize
# 9223372036854775807       # 63 bits, not 64
# >>> sys.maxint
# 9223372036854775807       # same, maxint is removed from Python 3
# >>> type(sys.maxsize)
# <type 'int'>
# >>> type(sys.maxsize+1)
# <type 'long'>
# >>> sys.maxsize.bit_length
# <built-in method bit_length of int object at 0x24067d8>
# >>> sys.maxsize.bit_length()
# 63

# http://stackoverflow.com/questions/9860588/maximum-value-for-long-integer
# Long integers have unlimited precision. In Python 2, Integers will automatically switch to longs when they grow beyond their limit:


 # class array.array(typecode[, initializer])

# list comprehensions:
# S = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# in other languages you can usually perform operations like:
#a[i]=0
# without having to worry if a[i] already exists. In many cases the cost of this facility is that you have to declare the size of the array using a dimension statement of some sort. Python doesn't have such a facility because lists are dynamic and don't have to be "dimensioned". It is fairly easy to do the same job as a dimension statement, however, using a "comprehension".

import array

def squares():
    #sqr = array.array("L", )    
    print "starting"
    before = datetime.datetime.now()
               #for i in range(1, 1000000001):
    sqr = [x**2 for x in range(1, 100000001)]
    #for i in range(1, 1001): sqr[i] = i**2
    #print sqr  - don't print this, even for 100000 - takes ages
    after = datetime.datetime.now()
    print "took " + str((after - before).seconds) + " seconds" # datetime.timedelta.microseconds(after - before)
    print "done"
    
now_string()
squares()
now_string()