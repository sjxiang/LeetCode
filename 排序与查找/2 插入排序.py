""" Insertion Sort """


"""
插入排序
    减治
"""
def insertion_sort(arr):
    # 分为已 、 未 排序与查找
    # 假设第 1 个元素已经排序，从第二个开始；
    # 已排序只有第 1 个元素，那么它肯定最小
    for i in range(1, len(arr)):
        item_to_insert  = arr[i]
        # 保留已排序的最后一个元素下标
        j = i - 1

        # 比它大的往后倒腾
        while j >= 0 and arr[j] > item_to_insert:
            arr[j+1] = arr[j]
            j -= 1

        # 再给它自己赋值
        arr[j+1] = item_to_insert

    return arr