""" Merge Sort """

"""
归并排序
    分治
"""
# 合并两个有序数组

def merge(sorted_a, sorted_b):
    i, j = 0, 0
    res = []

    while i < len(sorted_a) or j < len(sorted_b):
        if sorted_a[i] > sorted_b[j]:
            res.append(sorted_b[j])
            j += 1
        else:
            res.append(sorted_a[i])
            i += 1

    # 把剩余的塞进数组
    if i < len(sorted_a):
        res.expend(sorted_a[i:])
    else:
        res.extend(sorted_b[j:])

    # while i < len(sorted_a):        # append vs. expend
    #     res.append(sorted_a[i])
    #     i += 1

def mergesort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid = len(arr) // 2

        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])

        return merge(left, right)