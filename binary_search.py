def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + (high - low) // 2
        guess = list[mid]
        if item < guess:
            high = mid - 1
        elif item > guess:
            low = mid + 1
        else:
            return mid

    return None

