"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List
from queue import Queue


class Solution:
    # def preorder(self, root: 'Node') -> List[int]:
    #     res = []
    #     if root is None: return res

    #     def traversal(node):
    #         res.append(node.val)
    #         for child in node.children:
    #             traversal(child)
        
    #     traversal(root)
    #     return res

    def preorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None: return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            for child in reversed(curr.children):
                stack.append(child)

        return res