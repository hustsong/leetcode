# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val, q_val = p.val, q.val
        node = root

        while node:
            curr_val = node.val
            if curr_val > max(p_val, q_val):
                node = node.left
            elif curr_val < min(p_val, q_val):
                node = node.right
            else:
                return node
                
        return node

