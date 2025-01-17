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


def reverse_string(s):
    stk = Stack()
    for i in s:
        stk.push(i)
    res = ""
    while stk.size() != 0:
        res += stk.pop()
    return res


if __name__ == "__main__":

    print(reverse_string("We will conquere COVID-19"))
