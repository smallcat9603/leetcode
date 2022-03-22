#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new = [nums[0]]
        for i in range(1, len(nums)):
            if(nums[i] > new[-1]):
                new.append(nums[i])
        for i in range(len(new)):
            nums[i] = new[i]
        return len(new)
# @lc code=end

