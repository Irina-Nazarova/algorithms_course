class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            raise IndexError("Stack is empty")


def reverse_polish_notation(input_array):

    MATH = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a // b,
    }
    stack = Stack()

    for (element) in (input_array):
        if (element in MATH):
            up_number = (stack.pop())
            below_number = stack.pop()
            stack.push(MATH[element](below_number, up_number))

        else:
            try:
                stack.push(int(element))
            except ValueError:
                raise ValueError("Only integers are allowed")
    return stack.pop()


if __name__ == "__main__":
    string = input().split()
    print(reverse_polish_notation(string))
