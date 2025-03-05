def merge(left, right):
    result = []
    left_position, right_position = 0, 0

    while left_position < len(left) and right_position < len(right):
        if left[left_position] < right[right_position]:
            result.append(left[left_position])
            left_position += 1
        else:
            result.append(right[right_position])
            right_position += 1

    result.extend(left[left_position:])
    result.extend(right[right_position:])

    return result


def merge_sort(data):
    if len(data) <= 1:
        return data

    middle = len(data) // 2
    left = data[:middle]
    right = data[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)
