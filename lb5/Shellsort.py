def shell_sort(arr):

    gap = len(arr)//2

    while gap > 0:
        for i in range(gap, len(arr)):
            current_value = arr[i]
            position = i

            while position >= gap and arr[position - gap] > current_value:
                arr[position] = arr[position - gap]
                position -= gap
                arr[position] = current_value
        gap //= 2
    return arr