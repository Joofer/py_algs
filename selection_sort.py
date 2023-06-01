def min(arr):
    m = 0
    for i in range(0, len(arr)):
        if arr[i] < arr[m]:
            m = i
    return m

def selection_sort(arr):
    sorted = []
    for i in range(0, len(arr)):
        m = min(arr)
        sorted.append(arr[m])
        del arr[m]
    return sorted
