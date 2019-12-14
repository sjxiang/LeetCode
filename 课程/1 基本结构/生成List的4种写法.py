def test1():
    l = []
    for i in range(10):
        l = l + [i]


def test2():
    l = []
    for i in range(10):
        l.append(i)


def test3():
    l = [i for i in range(10)]


def test4():
    l = list(range(10))


if __name__ == "__main__":
    """
    list 连接最慢
    append 次之
    列表推导式 其次
    range函数 最快
    
    list 
        pop()
        pop(i)
    
    """
    pass