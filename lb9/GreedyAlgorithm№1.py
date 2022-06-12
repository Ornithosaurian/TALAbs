import numpy as np

weight = [35, 10 ,30, 60, 35, 25, 50, 30, 40, 10, 25, 45]
price = [10, 5 ,40, 30, 45, 65, 50, 25, 35, 60, 30, 15]
item = np.array(list(zip(weight,price)))
S = 170

def Weight(item):
	return np.lexsort([-1*item[:,1], item[:,0]])

def Price(item):
	return np.lexsort([item[:,0], -1*item[:,1]])

def Density(item):
	number = len(item)
	data_list = [0] * number
	for i in range(number):
		data_list[i] = (item[i,1])/(item[i,0])
	data_set = np.array(data_list)
	index = np.argsort(-1*data_set)
	return index

def Knapsack(item, S, index):
	number = len(item)
	status = [0] * number
	total_weight = 0
	total_value = 0
	for i in range(number):
		if item[index[i],0] <= S:
			total_weight += item[index[i],0]
			total_value += item[index[i],1]
			status[index[i]] = 1
			S -= item[index[i],0]
	return total_weight, total_value, status

print(item)
index_weight = Weight(item)
index_price = Price(item)
index_density = Density(item)
results_weight = Knapsack(item, S, index_weight)
print("Максимальна кількість предметів")
print(results_weight)
results_Price = Knapsack(item, S, index_price)
print("Максимальна сумарна вартість")
print(results_Price)
print("Щось середнє")
results_Density = Knapsack(item, S, index_density)
print(results_Density)