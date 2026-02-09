
class NodeTree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right



class BinaryTree:
    def __init__(self):
        self.root = None
        self.depth = 0

    def add(self, value):
        if self.root is None:
            self.root = NodeTree(value, None, None)
            self.depth += 1
            return
        current_node = self.root
        depth = 0
        while True:
            if current_node.value > value:
                if current_node.left != None:
                    current_node = current_node.left
                    self.depth += 1
                else:
                    current_node.left = NodeTree(value, None, None)
                    break
            else:
                if current_node.right != None:
                    current_node = current_node.right
                    self.depth += 1
                else:
                    current_node.right = NodeTree(value, None, None)
                    break
        return depth

def tree_sum(tree):
    summ = 0
    current_node = tree.root
    def dfs(current_node):
        if current_node == None:
            return
        summ += current_node.value
        dfs(current_node.left)
        dfs(current_node.right)
    return summ

def tree_max(tree):
    pass
def tree_min(tree):
    pass

def tree_contains(tree, value):
    pass






tree = BinaryTree()

tree.add(5)
tree.add(8)
tree.add(2)
tree.add(16)
print(tree.depth)
print(tree_sum(tree))
