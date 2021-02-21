# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
    #     res = []
    #     def dfs(node, target, rec):
    #         if node is None:
    #             return

    #         target -= node.val
    #         dfs(node.left, target, rec[:] + [node.val])
    #         dfs(node.right, target, rec[:] + [node.val])
    #         if node.left is None and node.right is None:
    #             if target == 0:
    #                 rec.append(node.val)
    #                 res.append(rec)

    #     dfs(root, targetSum, [])
    #     return res

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [(root, [root.val])]

        while stack:
            curr, path = stack.pop()
            if not curr.left and not curr.right and sum(path) == targetSum:
                res.append(path)
            if curr.right:
                stack.append((curr.right, path[:] + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, path[:] + [curr.left.val]))

        return res