def longest_repetition(chars):

    max = 0
    char = ''
    prev_char = None
    for i in range(len(chars)):
        if chars[i] == prev_char:
            count += 1
        else:
            count = 1
        if count > max:
            max = count
            char = chars[i]
        prev_char = chars[i]
    return (char, max)
