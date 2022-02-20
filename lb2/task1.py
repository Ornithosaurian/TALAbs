array = [1, 2, 3,'j', -4, 5, 6.5, 7, 8, 9, 10]

def recurse_sum(array, i, sum):
    if i == len(array):
        print(sum)
        return
    else:
        sum += array[i]
        recurse_sum(array, i + 1, sum)

def iteration_sum(array, sum):
    for i in range(len(array)):
        sum += array[i]

    print(sum)
    return

def print_sum(array):
    sum = 0
    for i in range (len(array)):
        if type(array[i])==str:

            return print("Error")

    iteration_sum(array, sum)
    recurse_sum(array, 0, sum)
print_sum(array)
