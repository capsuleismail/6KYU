def find_even_index(arr):

    for i in range(len(arr)):
        # divide the array in 2 with a one loop
        # because we need the index
        first = arr[:i]
        half = arr[i + 1:]

        # if the sum are same, we return which index is dividing first and half
        # basic think that I forgot and get me stuck is that when u slicing arr[:i] i is not included
        if sum(first) == sum(half):
            break
    else:
        return -1
    return i
