
class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self) -> str:
        return str(self.key)
    

class Tree:
    def __init__(self) -> None:
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, key):
        node = TreeNode(key)
        if self.is_empty():
            self.root = node 
        else:
            iter = self.root
            added = False 
            while not added:
                if iter.key > key:
                    if iter.left is None:
                        iter.left = node
                        node.parent = iter
                        added = True
                    else: 
                        iter = iter.left
                else:
                    if iter.right is None:
                        iter.right = node
                        node.parent = iter
                        added = True
                    else:
                        iter = iter.right

    def find(self, key):
        iter = self.root
        while iter is not None and iter.key != key:
            if iter.key > key:
                iter = iter.left
            else:
                iter = iter.right
        return iter
    
    def remove_leaf(self, node):
        if node == self.root:
            self.root = None
        elif node.parent.key > node.key:
            node.parent.left = None
        else:
            node.parent.right = None

    def remove_single_child(self, node):
        if node.parent.key > node.key:
            if node.left is not None:
                node.parent.left = node.left
            else:
                node.parent.left = node.right
        else:
            if node.left is not None:
                node.parent.right = node.left
            else:
                node.parent.right = node.right

    def get_successor(self, node):
        iter = node.right
        while iter.left is not None:
            iter = iter.left
        return iter

    def remove(self, key):
        node = self.find(key)
        if node is not None:
            # check leaf
            if node.left is None and node.right is None:
                self.remove_leaf(node)
            # check has single child
            elif node.left is None or node.right is None:
                self.remove_single_child(node)
            # check 2 children
            else:
                successor = self.get_successor(node)
                value = successor.key
                self.remove(value)
                node.key = value


    def inorder(self):
        stack = []
        iter = self.root
        while iter is not None or len(stack) > 0:
            if iter is None:
                iter = stack.pop(len(stack) - 1)
                print(iter, end=' ')
                iter = iter.right
            else:
                stack.append(iter)
                iter = iter.left
        print()

    def inorder_recursive(self, node): 
        if node is not None:
            self.inorder_recursive(node.left)
            print(node.key, end=' ')
            self.inorder_recursive(node.right)

    def postorder_recursive(self, node): 
        if node is not None:
            self.postorder_recursive(node.left)
            self.postorder_recursive(node.right)
            print(node.key, end=' ')

    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
            
if __name__ == "__main__":
    bst = Tree()
    keys = [100, 70, 150, 40, 80, 85, 120, 180]
    # keys = [100]
    for key in keys:
        bst.add(key)
    bst.inorder()
    bst.inorder_recursive(bst.root)
    print()
    bst.postorder_recursive(bst.root)
    print()
    # bst.remove(40)
    # bst.inorder()
    # bst.remove(70)
    # bst.inorder()
    bst.remove(100)
    bst.inorder()
    print(bst.height(bst.root))


