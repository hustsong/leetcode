# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -float('inf')
        def get_max(node):
            nonlocal res
            if node is None:
                return 0

            l_max = get_max(node.left)
            r_max = get_max(node.right)
            l_max = 0 if l_max < 0 else l_max
            r_max = 0 if r_max < 0 else r_max
            curr_sum = node.val + l_max + r_max
            
            res = curr_sum if curr_sum > res else res
            return node.val + max(l_max, r_max)
        
        get_max(root)
        return res
