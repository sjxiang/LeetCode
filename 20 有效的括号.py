# leetcode 20. 有效的括号

# 简单括号匹配

# e.g.
# 1  "()"、
# 2  "()[]"
# 3  "([]"
# 4  ")("

# 解法：栈
# 开括号，压栈
# 闭括号，先窥(None ?) 再判断

class Solution:
    def isValid(self, s):
        stack = []
        dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # 写法 1
        # for c in s:
        #     if c not in dict:
        #         stack.append(c)
        #     elif not stack or dict[c] != stack.pop():
        #         return False
        #
        # return not stack


        # 写法 2

        index = 0
        matched = True
        while index < len(s) and matched:
            char = s[index]
            if char in dict:
                stack.append(char)
            else:
                if stack is None:
                    matched = False
                else:
                    stack.pop()

            index += 1

        if matched and not stack:
            return True
        else:
            return False





import sys
print(sys.prefix)

import click
print(click)

"""
C:\Users\Administrator\AppData\Local\Programs\Python\Python36-32\

<module 'click' from 
'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36-32
\\lib\\site-packages\\click\\__init__.py'>

"""