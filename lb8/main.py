import Person as p
import string
from tree import BinarySearchTree as tree

# print(ord('a') - 97)
# print(ord('z') - 97)

objs = [tree() for i in range(26)]

def add(obj):
    objs[obj.flet].put(hash(obj),obj)

def get(obj):
    return objs[obj.flet].get(hash(obj))

p1 = p.Person("Vasys", "bubybc", 1)  # Dudybc

add(p1)
print(get(p1).flet)

# print(hash(p1))
