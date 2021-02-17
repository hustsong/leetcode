# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def inTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     if not root: return res

    #     def dfs(node):
    #         if node.left:
    #             dfs(node.left)
    #         res.append(node.val)
    #         if node.right:
    #             dfs(node.right)

    #     dfs(root)
    #     return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res

        stack = []
        curr = root
        while (stack or curr):
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
    






