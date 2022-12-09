#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
import itertools

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        tree = []
        for link in prerequisites:
            add_link_to_tree = True
            for path in tree:
                if link[0] == link[1]:
                    return False
                elif link[0] in path and link[1] in path and path.index(link[0]) > path.index(link[1]):
                    return False
                elif path[-1] == link[0]:
                    path.append(link[1])
                    add_link_to_tree = False
            if add_link_to_tree:
                tree.append(link)
        else:
            for idx1 in range(len(tree)-1):
                for pair1 in list(itertools.combinations(tree[idx1], 2)):
                    for idx2 in range(idx1+1, len(tree)):
                        for pair2 in list(itertools.combinations(tree[idx2], 2)):
                            if pair1[::-1] == pair2:
                                return False
            return True
        
# @lc code=end

