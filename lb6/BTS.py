class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.data = x


class Tree:
    root = None

    def __init__(self):
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
