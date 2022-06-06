import timeit as tt
import sys


t1a = '''
import bplus as bp

record_len = 1000
bplustree = bp.BplusTree(record_len)

'''
t1acode = '''

for i in range(1,1001):
    bplustree.insert(str(i), str(i))

'''

t1b = '''
import bplus as bp
import random

record_len = 1000
bplustree = bp.BplusTree(record_len)

with open("randelements", "w") as file:
    for i in range(1,1001):
        file.write(str(random.randint(-100000,100000)))
        file.write(" ")


'''
'''t1bcode = 
with open('randelements','r') as f:
    for line in f:
        for word in line.split():
           bplustree.insert(word,word)

'''

t3 = '''
import bplus as bp

record_len = 1000
bplustree = bp.BplusTree(record_len)

for i in range(1,1001):
    bplustree.insert(str(i), str(i))
'''
t3code = '''

bplustree.search("500")

'''

t4a = '''
import bplus as bp

record_len = 1000
bplustree = bp.BplusTree(record_len)

for i in range(1,1001):
    bplustree.insert(str(i), str(i))
'''
t4acode = '''

bplustree.delete("500","500")

'''
t4b = '''
import bplus as bp
import random

record_len = 1000
bplustree = bp.BplusTree(record_len)

with open("randelements", "w") as file:
    for i in range(1,1001):
        file.write(str(random.randint(-1000,1000)))
        file.write(" ")

with open('randelements','r') as f:
    for line in f:
        for word in line.split():
           bplustree.insert(word,word)

'''
t4bcode = '''

bplustree.delete("1000","1000")

'''
################################################################################################################

accuracy = 1
#
print('наповнення(послідовні): ', tt.timeit(t1acode, setup=t1a, number=accuracy) / accuracy)
print('наповнення(рандомні): ', tt.timeit(t1bcode, setup=t1b, number=accuracy) / accuracy)
print('пошук: ', tt.timeit(t3code, setup=t3, number=accuracy) / accuracy)
print('видалення: ', tt.timeit(t4acode, setup=t4a, number=accuracy) / accuracy)
# print('видалення(рандомні): ', tt.timeit(t4bcode, setup=t4b, number=accuracy) / accuracy)