""" Selection Sort"""

"""
选择排序
"""

def Selection_Sort(arr):
    # 已，未 排序序列
    # 初始化，已排序数目为 0，未排序为 len(arr)
    for i in range(len(arr)):
        # 假设未排序的，第 i 项为 Min
        min = i
        # 遍历未排序的项
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr




















"""
堆排序
3种：
    
    堆
    堆排序

"""


def heapsort_use_heapq(iterable):
    from heapq import heappush, heappop
    items = []
    for value in iterable:
        heappush(items, value)
    return [heappop(items) for i in range(len(items))]

