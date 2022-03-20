#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 
        'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        c = list(s)
        sum = 0
        jump = False
        for i in range(len(c)):
            if(jump == True):
                jump = False
                continue
            if(i<len(c)-1 and c[i]+c[i+1] in dict):
                sum += dict[c[i]+c[i+1]]
                jump = True
            else:
                sum += dict[c[i]]
        return sum  
# @lc code=end