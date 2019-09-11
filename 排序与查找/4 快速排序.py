""" Quick Sort """


"""
快速排序
    分治 三步
        分割
        子数组排序
        合并
    

快速排序的优化：
    空间：
        原地快排
        
    时间：
        性能依赖于基准值 Pivot
        三取样切分
            基准值为中位数最优
            一次取三个数，中间为基准值
            
与归并都是拆分，一个以下标，一个以数值大小
"""

def quick_sort(arr):
    if len(arr) < 2: # 递归出口，空数组或者数组长度为 1，都是有序的
        return arr
    else:
        pivot_index = 0
        pivot = arr[pivot_index]  # 选择第 1 个元素作为基准

        less_part = [i for i in arr[pivot_index+1:] if i <= pivot]  # 排除 基准值
        great_part = [i for i in arr[pivot_index+1:] if i > pivot]

        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test():
    import random
    arr = list(range(20))
    random.shuffle(arr)
    print(arr)
    # [10, 6, 11, 16, 9, 19, 3, 13, 0, 17, 4, 2, 1, 15, 12, 8, 18, 7, 5, 14]

    print(quick_sort(arr))
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert quick_sort(arr) == sorted(arr)

test()