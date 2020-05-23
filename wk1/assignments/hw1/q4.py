"""
Write a function that takes an integer x that is greater than 1 and returns the largest integer that is smaller than x and evenly divides x.
"""

def largest_factor(x):
    """Return the largest factor of x that is smaller than x.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    best = x - 1
    while x > 0:
        if x % best == 0:
            return best
        best = best - 1
