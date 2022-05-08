class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.data = x


class Tree:
    root = None

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        if x < self.root.data:
            if self.root.left is None:
                self.root.left = Tree()
            self.root.left.insert(x)
        else:
            if self.root.right is None:
                self.root.right = Tree()
            self.root.right.insert(x)

    def find(self, x):  # повертає вузол
        if self.root is None:
            return None
        if x == self.root.data:
            return self.root
        if x < self.root.data:
            if self.root.left is None:
                return None
            return self.root.left.find(x)
        else:
            if self.root.right is None:
                return None
            return self.root.right.find(x)

    def print(self):
        if self.root is None:
            return
        if self.root.left:
            self.root.left.print()
        print(self.root.data)
        if self.root.right:
            self.root.right.print()

    def delete(self, x):  # видаляє ноду Х і повертає рут

        if self.root.data == x:
            if self.root.right and self.root.left:
                # psucc - перент, succ - спадкоємець. Гет
                [psucc, succ] = self.root.right.findMin(self)

                if psucc.left == succ:  # об'єднання спадкоємця через перент
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right

                succ.left = self.left  # скидає спадкоємців
                succ.right = self.right  #
                return succ

            else:
                if self.root.left:
                    return self.root.left  # просування ліворуч
                else:
                    return self.root.right  # праворуч
        else:
            if self.root.data > x:
                if self.root.left:
                    self.root.left = self.root.left.delete(x)
            else:
                if self.root.right:
                    self.root.right = self.root.right.delete(x)

        return self

    def findMin(self, parent):  # шукає та повертає мін. ноду й рут
        if self.root.left:
            return self.root.left.findMin(self)
        else:
            return [parent, self]
