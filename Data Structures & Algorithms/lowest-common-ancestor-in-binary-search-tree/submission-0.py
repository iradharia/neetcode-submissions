# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
BFS or DFS?
- ancestor problem, going to go with DFS
- i think either way the ancestor is either going to be
        p <= ancestor < q or p < ancestor <= q

APPROACH (1)
- i want to first traverse the tree and FIND p, q
- as i traverse, i need to keep track of the previous roots
- when p and q are found, i need to find the root of the level before them or including their level if the ancestor is a descendant of itself

QUESTION:
if this is DFS, can i do it recursively? or would i need to do it iteratively

APPROACH (2) after ONE HINT:
traverse the tree in any order, when you find a node value that is in between min(p,q) < value< max(p,q)then you can return that as your lowest common ancestor!
"""


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p,q)










