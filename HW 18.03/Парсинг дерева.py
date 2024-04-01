class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def fromString(string):
        def parse_node(substring):
            if not substring:
                return None

            if substring[0] == '(':
                left_index = substring.index('(')
                right_index = substring.rindex(')')
                value = int(substring[:left_index])
                left_substring = substring[left_index:]
                right_substring = substring[right_index + 1:]
                node = TreeNode(value)
                if left_substring:
                    node.left = parse_node(left_substring)
                if right_substring:
                    node.right = parse_node(right_substring)
                return node
            else:
                return TreeNode(int(substring))

        string = string.replace(' ', '')
        nodes = string.split(';')
        return parse_node(nodes[0])


s = "10; (5; (3); (7)); (15; (); (20))"
parsed_tree = TreeNode.fromString(s)
print(parsed_tree.value)
