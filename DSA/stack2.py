import collections


class Stack:
    def __init__(self):
        self.container = collections.deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


def is_match(a, b):
    parantheses = {")": "(", "]": "[", "}": "{"}
    return parantheses[a] == b


def is_balanced(s):
    stk = Stack()
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stk.push(i)
        if i == ")" or i == "}" or i == "]":
            if stk.size() == 0:
                return False
            if not is_match(i, stk.pop()):
                return False
    return stk.size() == 0


if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
