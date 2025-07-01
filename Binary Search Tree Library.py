class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,root,data):
        if root is None:
            return BSTNode(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def search(self, root, key):
        if root is None or root.data == key:
            return root is not None
        if key < root.data:
            return self.search(root.left, key)
        return self.search(root.right, key)
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)