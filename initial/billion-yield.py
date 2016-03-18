# How would you write a function to compute the squares of numbers from 1 to 1 Billion inclusive in Python?

import numpy, array, logging, os, datetime

def billion_squares():    
    #numpy.array([x**2 for x in xrange(1, 100000001)]) # list comprehension
    # return
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

def square_generator(max):
    n = 1
    #while n < max:
    while True:
        yield n * n
        n += 1

#billion_squares()    

if __name__ == "__main__":
    if os.getenv('DEBUGGING'):
        logging.basicConfig(level=logging.INFO) # logging.DEBUG

    print "starting"

    before = datetime.datetime.now() # timeit.timeit(squares())
    

    max = 1000000000

    squares = array.array("L", ) # make somewhere to put them - might save time?
    gen = square_generator(max) # get the generator
    
    count = 0    
    for i in xrange(1, max + 1):
        #if i % 1000000 == 0:
            #print "1000000, count: "+str(count)
            #count = count+1

        # square = square_generator.next() # python 2
        square = next(gen) # python 3 - st2 Tools -> Build (F7) seems to be using Python3
        #print "square of " + str(i) + ": " + str(square)
        #squares.append(square)
    #print squares
    print "finished"
    after = datetime.datetime.now()
    print "took "+str((after - before).seconds)+" seconds/"+str((after - before).microseconds)+" microseconds"

"""

max = 100000000 (100 million)

starting
finished
took 42 seconds/655969 microseconds
[Finished in 42.9s]

max = 1000000000 (1 billion)

starting
[Finished in 286.0s with exit code -9]

(what is -9? standard error codes are all positive... 
or does it mean 9 

    #define EBADF            9      /* Bad file number */

    errno.EBADF                     # Bad file number

https://docs.python.org/2/library/errno.html
/usr/include/asm-generic/errno-base.h 
/usr/include/asm-generic/errno.h

>>> errno.errorcode
{1: 'EPERM', 2: 'ENOENT', 3: 'ESRCH', 4: 'EINTR', 5: 'EIO', 6: 'ENXIO', 7: 'E2BIG', 8: 'ENOEXEC', 9: 'EBADF', 10: 'ECHILD', 11: 'EAGAIN', 12: 'ENOMEM', ...
) 

http://stackoverflow.com/questions/1848729/why-return-a-negative-errno-e-g-return-eio

The problem is not so much that the stack is holding a billion squares and needs to generate with `yield`,
but that we're trying to store an array of a billion squares!

If you needed to do this in real life, you would either use a machine with more memory, or write to a file
- or "ask your boss why he wants a list of a billion squares"!

without appending to array:
starting
finished
took 262 seconds/475565 microseconds
[Finished in 263.9s]

How to do analysis of alorithms - what is O(n)? (Big O Notation)

"""