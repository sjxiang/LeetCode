class Queue:
    def __init__(self):
        # 基于 array 实现
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("队列为空")
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)


