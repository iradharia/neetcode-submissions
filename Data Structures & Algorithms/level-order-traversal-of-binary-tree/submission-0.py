# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                # check this node's left and right and
                # add them to the queue to process nex
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # append the current level to the ans array
            ans.append(level)
        return ans