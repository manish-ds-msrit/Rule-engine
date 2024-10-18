class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # 'operator' or 'operand'
        self.left = left  # left child
        self.right = right  # right child for operators
        self.value = value  # value for operand nodes

    def __repr__(self):
        return f'Node(type={self.type}, left={self.left}, right={self.right}, value={self.value})'

