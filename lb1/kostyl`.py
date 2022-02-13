def subsetUtil(arr, n, k, index, data, i):
    if (index == k):
        for j in range(k):
            print(data[j], end=" ")
        print(" ")
        return

    if (i >= n):
        return

    data[index] = arr[i]
    subsetUtil(arr, n, k, index + 1, data, i + 1)

    subsetUtil(arr, n, k, index, data, i + 1)


def subset(n, k):

    arr = [10, 20, 30, 40, 50]
    data = list(range(k))

    if(n < 1 or k < 1 or k == n):
        print("Тут трабл")
        return

    arr = list()
    for i in range(1, n + 1):
        arr.append(i)

    subsetUtil(arr, n, k,
                    0, data, 0)

print("1")
k = 5
n = 7
subset(n, k)
print("2")
k = - 8
n = 2
subset(n,k)
print("3")
k = 7
n = -8
subset(n,k)
print("4")
n = 5
k = n
subset(n,k)