# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = None
        def traverse(node, p, q):
            nonlocal res
            if node is None:
                return None
            if res is not None:
                return None

            left = traverse(node.left, p, q)
            right = traverse(node.right, p, q)
            if p in (node, left, right) and q in (node, left, right):
                res = node
                return None
            if p in (node, left, right):
                return p
            if q in (node, left, right):
                return q
            
        traverse(root, p, q)
        return res