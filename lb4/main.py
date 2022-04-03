from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from SelectionSort import selection_sort 

import numpy as np

bubble_sort(copy.copy(rand_1k))
bubble_sort(copy.copy(rand_10k))
bubble_sort(copy.copy(rand_100k))

bubble_sort(copy.copy(arr_1k))
bubble_sort(copy.copy(arr_10k))
bubble_sort(copy.copy(arr_100k))

insertion_sort(copy.copy(rand_1k))
insertion_sort(copy.copy(rand_10k))
insertion_sort(copy.copy(rand_100k))

insertion_sort(copy.copy(arr_1k))
insertion_sort(copy.copy(arr_10k))
insertion_sort(copy.copy(arr_100k))

selection_sort(copy.copy(rand_1k))
selection_sort(copy.copy(rand_10k))
selection_sort(copy.copy(rand_100k))

selection_sort(copy.copy(arr_1k))
selection_sort(copy.copy(arr_10k))
selection_sort(copy.copy(arr_100k))


arr = []

def make_random_arr(n):
    for i in range(n):
        arr.append(np.random.randint(n))
    return arr

rand_1k = make_random_arr(1000)
rand_10k = make_random_arr(10000)
rand_100k = make_random_arr(100000)

def make_arr(n):
    arr = np.arange(n)
    return arr

arr_1k = make_arr(1000)
arr_10k = make_arr(10000)
arr_100k = make_arr(100000)

#def make_random_uniq_arr(n):
#    arr = np.arange(n)
#    np.random.shuffle(arr)
#    return arr

#make_random_uniq_arr(100)
