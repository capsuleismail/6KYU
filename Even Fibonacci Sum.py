def even_fib(m):

    if m <= 2:
        return 0
    # start from two
    # forloop no bueno
    first = 0
    second = 2
    res = first + second

    while (second <= m):
        third = 4 * second + first
        # if we go further, stopbroski
        if (third >= m):
            break
        # move and update condition
        first = second
        second = third
        res = res + second
    return res
