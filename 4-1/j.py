def merge(a, b):
    l1 = list(a)
    l2 = list(b)
    result = []

    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))

    result.extend(l1)
    result.extend(l2)

    return tuple(result)
