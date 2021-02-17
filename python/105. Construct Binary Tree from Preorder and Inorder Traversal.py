# Definition for a binary tree node.

from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        pre_q = deque(preorder)
        in_map = {n:i for i, n in enumerate(inorder)}

        def build(start, end):
            if start > end: return None
            root = TreeNode(pre_q.popleft())
            root.left = build(start, in_map[root.val] - 1)
            root.right = build(in_map[root.val] + 1, end)
            return root

        return build(0, len(preorder) - 1)
