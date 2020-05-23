"""
Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

Pick a positive integer x as the start.
If x is even, divide it by 2.
If x is odd, multiply it by 3 and add 1.
Continue this process until x is 1.
The number x will travel up and down but eventually end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

Breaking News (or at least the closest thing to that in math). There has been a recent development in the hailstone conjecture that shows that almost all numbers will eventually get to 1 if you repeat this process. This isn't a complete proof but a major breakthrough

This sequence of values of x is often called a Hailstone sequence. Write a function that takes a single argument with formal parameter name x, prints out the hailstone sequence starting at x, and returns the number of steps in the sequence:
"""

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = x//2
        else:
            x = x * 3 + 1
        count = count + 1
    
    print(x)
    
    return count
