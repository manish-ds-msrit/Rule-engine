import re

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f'Node(type={self.type}, left={self.left}, right={self.right}, value={self.value})'

def create_rule(rule_string):
    tokens = re.split(r'(\s+|AND|OR|<|>|=|\(|\))', rule_string)
    tokens = [token.strip() for token in tokens if token.strip()]

    def parse_tokens(tokens):
        if not tokens:
            return None
        token = tokens.pop(0)
        if token == '(':
            left = parse_tokens(tokens)
            operator = tokens.pop(0)
            right = parse_tokens(tokens)
            tokens.pop(0)  # Remove closing parenthesis
            return Node(type='operator', left=left, right=right, value=operator)
        elif token.isdigit():
            return Node(type='operand', value=int(token))
        else:
            return Node(type='operand', value=token)

    return parse_tokens(tokens)

def combine_rules(rules):
    root = Node(type='operator', value='AND')
    left_node = create_rule(rules.pop(0))
    root.left = left_node
    right_node = combine_rules(rules) if rules else None
    root.right = right_node
    return root

def evaluate_rule(node, data):
    if node.type == 'operand':
        return data.get(node.value, None)
    elif node.type == 'operator':
        if node.value == 'AND':
            return evaluate_rule(node.left, data) and evaluate_rule(node.right, data)
        elif node.value == 'OR':
            return evaluate_rule(node.left, data) or evaluate_rule(node.right, data)
