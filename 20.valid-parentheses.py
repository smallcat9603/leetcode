#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '[':']', '{':'}'}
        ps = []
        for p in s:
            if(p in dict):
                ps.append(dict[p])
            elif(len(ps) > 0 and p == ps[-1]):
                ps.pop()
            else:
                return False
        return len(ps) == 0
# @lc code=end

