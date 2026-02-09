
class NodeTree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right



class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = NodeTree(value, None, None)
            return
        current_node = self.root
        while True:
            if current_node.value > value:
                if current_node.left is not None:

                    current_node = current_node.left
                else:
                    current_node.left = NodeTree(value, None, None)
                    break
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = NodeTree(value, None, None)
                    break

def tree_sum(tree):
    summ = 0
    current_node = tree.root
    def dfs(current_element):
        nonlocal summ
        if current_element is None:
            return 0
        summ += current_element.value
        dfs(current_element.left)
        dfs(current_element.right)
    dfs(current_node)
    return summ

def tree_elements(tree):
    elements = []
    current_node = tree.root

    def dfs(current_element):
        nonlocal elements
        if current_element is None:
            return
        elements.append(current_element.value)
        dfs(current_element.left)
        dfs(current_element.right)

    dfs(current_node)
    return elements

def tree_max(tree):
    return max(tree_elements(tree))

def tree_min(tree):
    return min(tree_elements(tree))

def tree_contains(tree, value):
    return value in tree_elements(tree)

tree = BinaryTree()

tree.add(5)
tree.add(8)
tree.add(2)
tree.add(16)

print(tree_sum(tree))
print(tree_max(tree))
print(tree_min(tree))
print(tree_contains(tree, 8))
print(tree_contains(tree, 7))
