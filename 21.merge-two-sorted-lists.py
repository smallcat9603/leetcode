#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = []
        l2 = []
        while(list1 is not None):
            l1.append(list1.val)
            list1 = list1.next
        while(list2 is not None):
            l2.append(list2.val)
            list2 = list2.next
        l3 = l1 + l2
        l3.sort()
        if(len(l3) > 0):
            list3 = ListNode(l3[0])
            cur = list3
            for i in range(1, len(l3)):
                cur.next = ListNode(l3[i])
                cur = cur.next
            return list3   
        else:
            return None
# @lc code=end

