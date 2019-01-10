# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        dotCount = 0
        for i in range(len(s)):
            if i != 0 and ((s[i] == '+' or s[i] == '-') and not (s[i - 1] == 'e' or s[i - 1] == 'E')):
                return False
            if i == 0 and not ('0' <= s[i] <= '9' or s[i] == '+' or s[i] == '-'):
                return False
            if not ('0' <= s[i] <= '9' or s[i] == '+' or s[i] == '-' or s[i] == '.' or s[i] == 'e' or s[i] == 'E'):
                return False
            if s[i] == '.':
                dotCount += 1
        if dotCount > 1:
            return False
        if s[-1] == 'e' or s[-1] == 'E':
            return False
        return True


s = Solution()
print(s.isNumeric('100'))
