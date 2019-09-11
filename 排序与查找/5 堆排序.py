""" heap Sort """

"""
堆排序：
    短时间实现比较困难，但可以借用 heapq 模块快速实现
"""
def heap_sort(arr):
    from heapq import heappush, heappop
    items = []

    for i in range(len(arr)):
        heappush(items, i)

    return [heappop(items) for i in range(len(items))]