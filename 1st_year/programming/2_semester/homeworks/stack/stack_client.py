from stack import Stack


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack2 = Stack(stack)
    stack2.pop()
    stack.pop()
    print(stack, stack2)


if __name__ == "__main__":
    main()