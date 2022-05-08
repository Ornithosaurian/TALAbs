from BST import Tree
from AVL import BalancedTree

binary_search_tree = Tree()

binary_search_tree.insert(5)
binary_search_tree.insert(6)
binary_search_tree.insert(7)
binary_search_tree.insert(1)
binary_search_tree.insert(10)
binary_search_tree.insert(30)
print("binary_search_tree")
print(binary_search_tree.find(5))
print(binary_search_tree.find(2))
binary_search_tree.print()
print("Видаляємо 1, 6, 30 і отримуємо таке дерево:")
binary_search_tree.delete(1)
binary_search_tree.delete(6)
binary_search_tree.delete(30)
binary_search_tree.print()

####
balanced_binary_search_tree = BalancedTree()
root = None
print("\nself-balancing binary search tree")
root = balanced_binary_search_tree.insert(root, 117)
root = balanced_binary_search_tree.insert(root, 3)
root = balanced_binary_search_tree.insert(root, 56)
root = balanced_binary_search_tree.insert(root, 409)
root = balanced_binary_search_tree.insert(root, 17)
root = balanced_binary_search_tree.insert(root, 218)

root = balanced_binary_search_tree.delete(root, 409)
balanced_binary_search_tree.print(root)
print(balanced_binary_search_tree.find(root, 56))