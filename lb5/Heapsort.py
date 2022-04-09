def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sift_down(arr, i, upper):
    while True:
        left = i*2+1
        right = i*2+2
        if max(left, right) < upper:
            if arr[i] >= max(arr[left], arr[right]):
                break
            elif arr[left] > arr[right]:
                swap(arr, i, left)
                i = left
            else:
                swap(arr, i, right)
                i = right
        elif left < upper:
            if arr[left] > arr[i]:
                swap(arr, i, left)
                i = left
            else: 
                break 
        elif right < upper:
            if arr[right] > arr[i]:
                swap(arr, i, right)
                i = right
            else:
                break
        else:
            break

def heap_sort(arr):
    for i in range((len(arr)-2)//2, -1, -1):
        sift_down(arr, i, len(arr))

    for end in range(len(arr)-1, 0, -1):
        swap(arr, 0, end)
        sift_down(arr, 0, end)
    return arr