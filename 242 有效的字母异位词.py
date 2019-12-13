# leetcode 242. 有效的字母异位词

# 变位词
# e.g. "python" or "typhon"


class Solution:
    def isAnagram(self, s, t):

        # 解法 1：排序比较
        # nlogn
        # return sorted(s) == sorted(t)

        # 解法 2：暴力枚举
        # n!

        # 解法 3：计数
        # n
        # 数组
        # arr_1 = [0] * 26
        # arr_2 = [0] * 26
        #
        # for item in s:
        #     arr_1[ord(item) - ord("a")] += 1
        # for item in s:
        #     arr_2[ord(item) - ord("a")] += 1
        #
        # j = 0
        # stillOK = True
        # while j < 26 and stillOK:
        #     if arr_1[j] == arr_2[j]:
        #         j += 1
        #     else:
        #         stillOK = False
        #
        # return stillOK

        # 哈希表
        # d1, d2 = {}, {}
        #
        # for i in s:
        #     if i not in d1:
        #         d1[i] = 1
        #     else:
        #         d1[i] += 1
        #
        # for i in t:
        #     if i not in d2:
        #         d2[i] = 1
        #     else:
        #         d2[i] += 1
        #
        # return d1 == d2

        pass


