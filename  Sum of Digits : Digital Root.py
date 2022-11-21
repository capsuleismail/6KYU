def digital_root(n):
    sm = sum([int(number) for number in str(n)])
    if len(str(n)) >= 2:
        sm = digital_root(sm)
    return sm
