def is_prime(x):
    return all(x % i for i in range(2, (x // 2) + 1))


def prime_bef_aft(num):
    please = num + 1
    while not is_prime(please):
        please += 1
    # creating a variable for each case prev and after will be much easier
    prev = num - 1
    while not is_prime(prev):
        prev -= 1

    return [prev, please]
