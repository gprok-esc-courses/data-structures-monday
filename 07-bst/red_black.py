
class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'

    def __str__(self) -> str:
        return str(self.key)
    

class RedBlackTree:
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
        self.insert_fixup(node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x 
        y.parent = x.parent
        if x.parent is None:    # x was root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y 
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x 
        y.parent = x.parent
        if x.parent is None:    # x was root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y 
        y.right = x
        x.parent = y

    def insert_fixup(self, z):
        while z.parent is not None and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:        # parent is LEFT child of grandparent
                y = z.parent.parent.right
                if y is not None and y.color == 'red':  # CASE 1
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.right:               # CASE 2
                    z = z.parent
                    self.left_rotate(z)
                else:                                   # CASE 3
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:                                       # parent is RIGHT child of grandparent
                y = z.parent.parent.left
                if y is not None and y.color == 'red':  # CASE 1
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.left:               # CASE 2
                    z = z.parent
                    self.right_rotate(z)
                else:                                  # CASE 3
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
        self.root.color = 'black'

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
    bst = RedBlackTree()
    for key in range(10000000):
        bst.add(key)
    print(bst.height(bst.root))


