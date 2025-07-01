class BinaryNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data):
        self.root = BinaryNode(root_data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end='')
            self.inorder(node.right)


    def preorder(self,node):
        if node:
            print(node.data, end='')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end='')