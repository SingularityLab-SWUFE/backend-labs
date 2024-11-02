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


def sum_digits(y: float ) -> int:
    a = '{:.0f}'.format(y) 
    total = 0
    for char in a:
        if char.isdigit():  
            total += int(char)
    return total
    pass


def double_eights(n: int) -> bool:
    """
    Return True if n has two eights in a row.
    """
    a=str(n)
    return '88' in a           
    pass