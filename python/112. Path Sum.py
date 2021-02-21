# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        res = False
        def dfs(node, sum):
            nonlocal res, targetSum
            if res:
                return
            if node is None:
                return

            curr_sum = sum + node.val
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            if node.left is None and node.right is None:
                if sum + node.val == targetSum:
                    res = True

        dfs(root, 0)
        return res