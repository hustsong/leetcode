# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        curr = root
        stack = []
        res = 0

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr_val = curr.val
            if curr_val >= low and curr_val <= high:
                res += curr_val
            if curr_val == high:
                break
            curr = curr.right

        return res