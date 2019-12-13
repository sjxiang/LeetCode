""" 540. 有序数组中的单一元素 """


class Solution:
    def singleNonDuplicate(self, nums):
        # if len(nums) == 0:
        #     return None
        #
        # filter = {}
        #
        # for i in nums:
        #     if i in filter:
        #         filter[i] += 1
        #     else:
        #         filter[i] = 1
        #
        # for key, value in filter.items():
        #     if value == 1:
        #         return key

        pass
"""
套路：hash table 统计

艹 题目还有要求：
    O(log n) 时间
    O(1)     空间

    二分查找
    
        递归
    
    如题，肯定有单个，那么数组长度 N，肯定是奇数
    
    o—————————o—————————o
             Mid
    
    那么 N - 1，是偶数
    (N - 1)/2  奇/偶 ?
    奇
        Arr(Mid - 1) == Arr(Mid) 单数在下标 Mid 后面
        否则，相反；
        进一步缩小范围
        
    偶
        就是 Mid        
"""