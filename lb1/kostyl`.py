def subsetUtil(array, n, k, index, subset, i):
    if (index == k):
        for j in range(k):
            print(subset[j], end=" ")
        print(" ")
        return

    if (i >= n):
        return

    subset[index] = array[i]
    subsetUtil(array, n, k, index + 1, subset, i + 1)

    subsetUtil(array, n, k, index, subset, i + 1)


def subset(n, k):

    subset = list(range(k))

    if(n < 1 or k < 1 or k == n):
        print("Тут трабл")
        return

    array = list()
    for i in range(1, n + 1):
        array.append(i)

    subsetUtil(array, n, k,
                    0, subset, 0)

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
