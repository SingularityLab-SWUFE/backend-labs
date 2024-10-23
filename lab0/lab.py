def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.
    """
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c


def sum_digits(y: int) -> int:
    """
    Sum all the digits of y.
    """
    pass


def double_eights(n: int) -> bool:
    """
    Return True if n has two eights in a row.
    """
    pass