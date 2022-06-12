import numpy as np

P = [1,2,3,4,5]
C = [2,5,8,9,6]
item = np.array(list(zip(P,C)))
V = [4,5,2]

def Resource(item):
	return np.lexsort([-1*item[:,1], item[:,0]])

def VirtualMachine(item, V, index):
	number = len(item)
	status = [0] * number
	for i in range(number):
		for j in range(len(V)):
			if item[index[i],1] == V[j]:
				status[index[i]] = item[index[i],0]
				V.remove(V[j])
				break
	if len(V) != 0:
		for i in range(number):
			for j in range(len(V)):
				if status[i] == 0 and item[index[i],1] > V[j]:
					status[index[i]] = item[index[i],0]
					V.remove(V[j])
					break
	return status

print(item)
index_resource = Resource(item)
results_resource = VirtualMachine(item, V, index_resource)
print(results_resource)