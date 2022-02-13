def combinationUtil(arr, n, k,
                    index, data, i):
    # Current combination is
    # ready to be printed,
    # print it

    if (index == k):
        for j in range(k):
            print(data[j], end=" ")
        print(" ")
        return

    # When no more elements
    # are there to put in data[]
    if (i >= n):
        return

    # current is included,
    # put next at next
    # location
    data[index] = arr[i]
    combinationUtil(arr, n, k,
                    index + 1, data, i + 1)

    # current is excluded,
    # replace it with
    # next (Note that i+1
    # is passed, but index
    # is not changed)
    combinationUtil(arr, n, k, index,
                    data, i + 1)


# The main function that
# prints all combinations
# of size r in arr[] of
# size n. This function
# mainly uses combinationUtil()
def printcombination(arr, n, r):
    # A temporary array to
    # store all combination
    # one by one
    data = list(range(r))

    if(k>n):
        print("Тут трабл")
        return

    arr = list()
    for i in range(1, n + 1):
        arr.append(i)


    # Print all combination
    # using temporary
    # array 'data[]'
    combinationUtil(arr, n, r,
                    0, data, 0)


# Driver Code
arr = [10, 20, 30, 40, 50]

k = 4
n = len(arr)
printcombination(arr, n, k)

# This code is contributed
# by Ambuj sahu