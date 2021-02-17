# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     res = []
    #     if not root: return res

    #     def dfs(node):
    #         res.append(node.val)
    #         if node.left:
    #             dfs(node.left)
    #         if node.right:
    #             dfs(node.right)

    #     dfs(root)
    #     return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root: return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return res
    






