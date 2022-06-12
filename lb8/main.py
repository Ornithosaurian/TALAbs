import Person as Person

from tree import BinarySearchTree as Tree

# print(ord('a') - 97)
# print(ord('z') - 97)

objects = [Tree() for i in range(26)]


def add(object):
    objects[object.flet].put(hash(object), object)


def search(object):
    return objects[object.flet].get(hash(object))


p1 = Person.Person("name", "cgviv", 21)  # Dudybc

add(p1)
print(search(p1).flet)

print(hash(p1))
