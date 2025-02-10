def to_string(*args, sep=' ', end='\n'):
    return sep.join(str(item) for item in args) + end
