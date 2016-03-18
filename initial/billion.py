# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
 
import datetime
 
def now_string():
    return datetime.datetime.isoformat(datetime.datetime.now())

print "started at "+now_string()

# How would you write a function to compute the squares of numbers from 1 to 1 Billion inclusive in Python?

# Long signed integer type. Capable of containing at least the [−2147483647, +2147483647] range;[3][4] thus, it is at least 32 bits in size.

# https://docs.python.org/2/library/array.html
# array — Efficient arrays of numeric values
# 'L'	unsigned long	long	4

# 4 bytes - 32 bits 2**32 = 4294967296 (4.2 billion - big enough for the number 1 billion, but not its square!)

# 1681000000000000

#>>> 41000000**2
#1681000000000000
#>>> a = 1681000000000000
#>>> 50000000**2
#2500000000000000
#>>> 5000000000**2
#25000000000000000000L

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
import numpy
import timeit
import sys

def squares():
    sqr = array.array("L")
    count = 0    
    for i in xrange(1, 5000001):
        if i % 1000000 == 0:
            print "1000000, count: "+str(count)
            count = count+1
        sqr.append(i**2)
    return sqr

# 1billion squared is:
# 1000000000000000000
# 2**63
# 9223372036854775808
# 2**60
# 1152921504606846976
# so 60 bits?
# 7 bytes
# 1 billion * 7 bytes = 7Gb?
# but it falls over even when each element is 0
# array() initialised with "L" meaning unsigned long int - 4 bytes
# 1 billion * 4 bytes = 4Gb?


# how wide would a location need to be to hold the square of a billion?
def base2():
    for i in range(1, 64):
        print "i: "+str(i)+" - "+str(2**i)

#base2()
#sys.exit(0)

def squares_test():
    print "starting"
    
    numpy.array([x**2 for x in xrange(1, 100000001)])
    return
    sqr = array.array("L", ) # unsigned long int
    #sqr = array.array("H", ) # unsigned short int "OverflowError: unsigned short is greater than maximum"
    #sqr = array.array("I", ) # unsigned int "OverflowError: unsigned int is greater than maximum"
    count = 0    
    for i in xrange(1, 50000001):
        if i % 1000000 == 0:
            print "1000000, count: "+str(count)
            count = count+1
        sqr.append(i**2)
    return sqr
        #x.append(0)
    # 10000001:  3 seconds/831881 microseconds
    # 20000001:  7 seconds
    # 30000001:  11 seconds    
    # 40000001:  15 seconds    
    # 50000001:  falls over at about 41000000?
            # 41000000**2 == 1681000000000000 
    # 100000001: hangs?
    # gets further under Windows, can handle 50M but not 500M
    # actually it seems to be the range itself that causes a problem, not the array or its contents
    # xrange() better - appending 0, gets to 238000000 before MemoryError
    # "xrange() works for 10-digit numbers" 
    # xrange() appending i**2 also gets to 238000000 before MemoryError
    
    # 1 billion + 1 = 1000000001
               #for i in range(1, 1000000001):
    #x = [0] * 100000000 # took 0 seconds/783561 microseconds
    #x = [0] * 200000000 # falls over with MemoryError!
    #numpy.array([x**2 for x in range(1, 10000001)]) # 2 seconds/380341 microseconds
    #numpy.array([x**2 for x in range(1, 100000001)]) # hangs?
    
    
    #sqr = [x**2 for x in range(1, 10000001)] # took 1 seconds/532346 microseconds
    #for i in range(1, 1001): sqr[i] = i**2
    #print sqr  - don't print this, even for 100000 - takes ages
    print "done"

before = datetime.datetime.now()
#timeit.timeit(squares())
sqr = squares_test()
after = datetime.datetime.now()
print "took "+str((after - before).seconds)+" seconds/"+str((after - before).microseconds)+" microseconds"
