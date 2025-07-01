class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []

    def add_child(self,child_node):
        self.children.append(child_node)

    def print_tree(self,level=0):
        print(" " * level * 2 + str(self.data))
        for child in self.children:
            child.print_tree(level+1)


root = TreeNode("Electronics")
laptop = TreeNode("Laptop")
phone = TreeNode("Phone")
tv = TreeNode("TV")

laptop.add_child(TreeNode("Dell"))
laptop.add_child(TreeNode("HP"))
phone.add_child(TreeNode("Samsung"))
phone.add_child(TreeNode("iPhone"))

root.add_child(laptop)
root.add_child(phone)
root.add_child(tv)

print("General Tree:")
root.print_tree()
