def is_prime(number):
    is_simple, i = True, 2

    if number > 1:
        while i <= number ** 0.5 and is_simple:
            if number % i == 0:
                is_simple = False
            i += 1
    else:
        is_simple = False

    return is_simple
