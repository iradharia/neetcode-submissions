# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p,q)])
        while queue:
            elem = queue.popleft()
            p = elem[0]
            q = elem[1]
            if p is None and q is None:
                continue
            if p is None and q:
                return False
            if q is None and p:
                return False
            if p.val != q.val:
                return False
            if p.val == q.val:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True