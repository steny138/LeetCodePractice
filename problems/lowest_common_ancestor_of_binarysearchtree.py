# 235 Lowest Common Ancestor of a Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val == p.val or root.val == q.val:
            return root
       
        if (p.val < root.val and root.val < q.val) or (p.val > root.val and root.val > q.val):
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return self.lowestCommonAncestor(root.right, p, q)
        
if __name__ == '__main__':
    pass