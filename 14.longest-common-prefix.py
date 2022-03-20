#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c = list(strs[0])
        for i in range(1, len(strs)):
            letters = list(strs[i])
            for j in range(len(c)):
                if(j > len(letters)-1):
                    c = letters
                    break
                if(c[j] != letters[j]):
                    c = c[:j]
                    break
            if(len(c) == 0):
                break
        return ''.join(c)
# @lc code=end

