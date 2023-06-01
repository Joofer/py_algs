def sum(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum(list[1:])
