from sympy import im
from Quicksort import quick_sort
from Mergesort import merge_sort
from Shellsort import shell_sort
from Heapsort import heap_sort

import numpy as np
import copy


arr = []

def make_random_arr(n):
    for i in range(n):
        arr.append(np.random.randint(n))
    return arr

rand_100k = make_random_arr(100000)
rand_1m = make_random_arr(1000000)

def make_arr(n):
    arr = np.arange(n)
    return arr
  
arr_100k = make_arr(100000)
arr_1m = make_arr(1000000)

rand_100k_copy = copy.copy(rand_100k)
rand_1m_copy = copy.copy(rand_1m)
arr_100k_copy = copy.copy(arr_100k)
arr_1m_copy = copy.copy(arr_1m)

quick_sort(rand_100k_copy)
quick_sort(rand_1m_copy)
quick_sort(arr_100k_copy)
quick_sort(arr_1m_copy)

merge_sort(rand_100k_copy)
merge_sort(rand_1m_copy)
merge_sort(arr_100k_copy)
merge_sort(arr_1m_copy)

shell_sort(rand_100k_copy)
shell_sort(rand_1m_copy)
shell_sort(arr_100k_copy)
shell_sort(arr_1m_copy)

heap_sort(rand_100k_copy)
heap_sort(rand_1m_copy)
heap_sort(arr_100k_copy)
heap_sort(arr_1m_copy)
