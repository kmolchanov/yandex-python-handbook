def make_matrix(size, value=0):
    if isinstance(size, tuple):
        x, y = size[0], size[1]
    else:
        x = y = size

    return [[value for _ in range(x)] for _ in range(y)]
