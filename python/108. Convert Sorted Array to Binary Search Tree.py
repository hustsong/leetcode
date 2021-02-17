# Definition for a binary tree node.

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        pivot = len(nums) // 2
        root = TreeNode(nums[pivot])
        root.left = self.sortedArrayToBST(nums[:pivot])
        if pivot < len(nums) - 1:
            root.right = self.sortedArrayToBST(nums[pivot + 1:])

        return root




