# n.b. don't call this file "doctest.py" as it will be seen as a module and override 

def cube(x):
    """
    >>> cube(10)
    1000
    """
    return x * x

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()