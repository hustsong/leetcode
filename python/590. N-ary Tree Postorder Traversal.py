"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List


class Solution:
    # def postorder(self, root: 'Node') -> List[int]:
    #     res = []
    #     if root is None: return res

    #     def traversal(node):
    #         for child in node.children:
    #             traversal(child)
    #         res.append(node.val)
    #     traversal(root)
    #     return res

    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None: return res
        
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            for child in curr.children:
                stack.append(child)

        return res[::-1]