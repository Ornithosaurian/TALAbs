def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    element = arr[0]

    left = list(filter(lambda x: x < element, arr))
    center = list(filter(lambda x: x == element,arr))
    right = list(filter(lambda x: x > element, arr))

    return quick_sort(left) + center + quick_sort(right)