""" Binary Search """


def binary_search():
    pass


# 二分查找
# 经常要求手写，注意边界
def binary_search(nums, key):
    if not nums:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right)
        if nums[mid] == key:
            return mid
        elif nums[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def binary_search_recurive(nums, left, right, key):
    if left >= end:
        return -1
    mid = (left + right) // 2
    if nums[mid] == key:
        return mid
    elif nums[mid] > key:
        return binary_search_recurive(nums, left, mid, key)  # 区间：左闭右开
    else:
        return binary_search_recurive(nums, mid, right, key)
