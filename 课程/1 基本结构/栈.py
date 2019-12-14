class Stack:
    def __init__(self):
        # 基于 array 实现
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("栈为空")
        else:
            self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("栈为空")
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)


def test():
    s = Stack()
# 争议：何为栈顶 何为栈底



if __name__ == "__main__":
    test()