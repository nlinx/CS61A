# CS 61A Fall 2014
# Name:
# Login:


def two_equal(a, b, c):
    """Return whether exactly two of the arguments are equal and the
    third is not.

    >>> two_equal(1, 2, 3)
    False
    >>> two_equal(1, 2, 1)
    True
    >>> two_equal(1, 1, 1)
    False
    >>> result = two_equal(5, -1, -1) # return, don't print
    >>> result
    True

    """
    return (a == b and b != c) or (a == c and b != c) or (b == c and a != c)


def same_hailstone(a, b):
    """Return whether a and b are both members of the same hailstone
    sequence.

    >>> same_hailstone(10, 16) # 10, 5, 16, 8, 4, 2, 1
    True
    >>> same_hailstone(16, 10) # order doesn't matter
    True
    >>> result = same_hailstone(3, 19) # return, don't print
    >>> result
    False

    """
    def in_hailstone(a,b):
        while a > 1:
            if a == b:
                return True
            elif a % 2 == 0:
                a = a // 2
            else:
                a = a * 3 +1

        return False

    return in_hailstone(a,b) or in_hailstone(b,a)


def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    >>> near_golden(18)
    3
    >>> near_golden(20)
    4
    >>> near_golden(22)
    4
    >>> near_golden(24)
    5
    >>> near_golden(26)
    5
    >>> near_golden(28)
    5
    >>> near_golden(30)
    6
    >>> near_golden(32)
    6
    >>> near_golden(34)
    7
    >>> near_golden(36)
    7
    >>> near_golden(38)
    7
    >>> near_golden(40)
    8

    """
    h = 1
    w = (perimeter / 2 - h)
    difference = abs((h/w) - (w/h - 1))
    while difference >= 0.001:
        h+=1
        w = (perimeter / 2 -h)
        nextDiff = abs((h/w) - (w/h - 1))
        if nextDiff > difference:
            return h-1
        difference = nextDiff
    return h



