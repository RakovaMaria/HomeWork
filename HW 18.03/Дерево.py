class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_to_string(root):
    if root is None:
        return ""
    result = str(root.value)
    if root.left or root.right:
        result += "; ("
        result += tree_to_string(root.left)
        result += ");"
        result += " ("
        result += tree_to_string(root.right)
        result += ")"
    return result


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print(tree_to_string(root))
