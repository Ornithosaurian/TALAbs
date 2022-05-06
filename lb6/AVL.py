class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.height = 1


class BalancedTree:

    def insert(self, root, x):

        if not root:
            return Node(x)
        elif x < root.data:
            root.left = self.insert(root.left, x)
        else:
            root.right = self.insert(root.right, x)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.balance(root)

        if balance > 1 and x < root.left.data:
            return self.rotate_right(root)

        if balance < -1 and x > root.right.data:
            return self.rotate_left(root)

        if balance > 1 and x > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and x < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, x):

        if not root:
            return root

        elif x < root.data:
            root.left = self.delete(root.left, x)

        elif x > root.data:
            root.right = self.delete(root.right, x)

        else:
            if root.left is None:
                tmp = root.right

                return tmp

            elif root.right is None:
                tmp = root.left

                return tmp

            tmp = self.min_data(root.right)
            root.data = tmp.data
            root.right = self.delete(root.right, tmp.data)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self.rotate_right(root)

        if balance < -1 and self.balance(root.right) <= 0:
            return self.rotate_left(root)

        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def min_data(self, root):
        if root is None or root.left is None:
            return root

        return self.min_data(root.left)

    def rotate_right(self, r):

        y = r.left
        tree3 = y.right

        y.right = r
        r.left = tree3

        r.height = 1 + max(self.get_height(r.left), self.get_height(r.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_left(self, r):

        y = r.right
        tree2 = y.left

        y.left = r
        r.right = tree2

        r.height = 1 + max(self.get_height(r.left), self.get_height(r.right))
        r.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def print(self, root):
        if root is None:
            return

        print(root.data)
        self.print(root.left)
        self.print(root.right)

    def find(self, root, x):
        if root is None:
            return False
        elif root.data == x:
            return True
        elif root.data < x:
            return self.find(root.right, x)
        return self.find(root.left, x)
