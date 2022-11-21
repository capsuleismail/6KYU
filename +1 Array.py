def up_array(arr):
    if not arr or any(x < 0 or x > 9 for x in arr):
        return None
    n = int(''.join([str(y) for y in arr])) + 1
    return [int(n) for n in str(n).zfill(len(arr))]


print(up_array([0, 4, 2]))
print(up_array([0, 4, 3]))
print(up_array([0, 4, 4]))
print(up_array([0, 1, 9, 8, 7]))
print(up_array([9, 9, 9]))
print(up_array([0, 0, 8, 4, 6, 7, 4, 0, 9, 6, 2, 3, 0, 0, 1, 0, 1, 2, 2, 5]))
print(up_array([0, 8, 4, 6, 7, 4, 0, 9, 6, 2, 3, 0, 0, 1, 0, 1, 2, 2, 5]))
