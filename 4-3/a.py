def recursive_sum(*numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + recursive_sum(*numbers[1:])
