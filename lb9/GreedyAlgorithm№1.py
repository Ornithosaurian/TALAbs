from pickle import NONE
import numpy as np

P = [1, 2, 3, 4, 5]
C = [2, 5, 8, 9, 6]
item = np.array(list(zip(P, C)))
V = [8, 5, 6]


def Resource(item):
    return np.lexsort([-1 * item[:, 1], item[:, 0]])


def VirtualMachine(item, V, index):
    number = len(item)
    status = [0] * len(V)
    for i in range(number):
        for j in range(len(V)):
            if item[index[i], 1] == V[j]:
                status[index[j]] = item[index[i], 0]
                break
    for i in range(number):
        for j in range(len(V)):
            if status[j] != 0 and status[j] != item[index[i], 0] and item[index[i], 1] > V[j]:
                status[index[j]] = item[index[i], 0]
                break
    return status


print(item)
index_resource = Resource(item)
results_resource = VirtualMachine(item, V, index_resource)
print(results_resource)
