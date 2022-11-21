def one_two_three(n):
    a, b = divmod(n, 9)
    return [int('0' + '9' * a + str(b) * bool(b)), int('0' + '1' * n)]


print(one_two_three(19))
print(one_two_three(143))
print(one_two_three(21))
print(one_two_three(22))
