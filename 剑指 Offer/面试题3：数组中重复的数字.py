# leetcode 442. 数组中重复的数据
# PS：其实和 LeetCode-442 还是有些差异，区别在于数据是 (1, n-1)


class Solution:
    def findDuplicates(self, nums):
        # 法 2
        dic = {}
        for item in nums:
            if item in dic.keys():
                dic[item] += 1
            else:
                dic[item] = 1

        res = []
        for key in dic.keys():
            if dic[key] == 2:
               res.append(key)
        return res

        # 法 3
