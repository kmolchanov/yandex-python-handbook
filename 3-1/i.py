while string := input():
    comment_position = string.find('#')
    if comment_position == -1:
        print(string)
    elif comment_position == 0:
        continue
    else:
        print(string[:comment_position])
