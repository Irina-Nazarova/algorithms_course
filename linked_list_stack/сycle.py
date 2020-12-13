class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


# —оздаем объекты
n3 = Node("third")
n2 = Node("second")
n1 = Node("first")

# —оздаем св€занный список из созданных ранее объектов
# n1.next = n2
# n2.next = n3
# n3.next = None

n1.next = n2
n2.next = n3
n3.next = n1  # loop


def hasCycle(node):
    if node == None:
        return False

    # ќбъ€вл€ем две переменные, которые будут соревноватьс€ в скорости прохождени€ цикла
    fast = node
    slow = node

    while fast is not None:
        if fast.next is not None:
            fast = fast.next.next
        else:
            return False
        slow = slow.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    print(hasCycle(n1))
