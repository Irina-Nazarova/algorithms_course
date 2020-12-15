class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


# right
n0 = Node(value=0)
n1 = Node(value=1)

n6 = Node(value=6, left=n0, right=n1)
n2 = Node(value=2, left=None, right=None)

# left
n103 = Node(value=3)

n14 = Node(value=14)
n15 = Node(value=15)

n8 = Node(value=8, left=n14, right=n15)
n10 = Node(value=10, left=None, right=n103)

n3 = Node(value=3, left=n8, right=n10)
n5 = Node(value=5, left=n2, right=n6)
n1 = Node(value=1, left=n3, right=n5)


def solution(Node, max_value=None) -> int:

    if max_value is None:
        max_value = Node.value

    if max_value < Node.value:
        max_value = Node.value

    if Node.left is not None:
        max_value = solution(Node.left, max_value)

    if Node.right is not None:
        max_value = solution(Node.right, max_value)
    return max_value


print(solution(Node=n1))