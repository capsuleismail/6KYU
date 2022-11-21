def find_outlier(integers):
    first = list(filter(lambda x: x % 2 == 0, integers))
    second = list(filter(lambda x: x % 2 != 0, integers))
    return first[0] if len(first) == 1 else second[0]
