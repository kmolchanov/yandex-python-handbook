def recursive_digit_sum(number):
    if number >= 10:
        return number % 10 + recursive_digit_sum(number // 10)
    else:
        return number
