# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set([node.val for node in nodes])
        res = None
        def path(node):
            if node is None:
                return []
            
            nonlocal res, nodes
            if res is not None:
                return []

            left = path(node.left) if node.left else []
            right = path(node.right) if node.right else []
            curr = left[:] + right[:]
            if node.val in nodes:
                curr.append(node.val)

            if len(curr) == len(nodes):
                if res is None:
                    res = node
            return curr

        path(root)
        return res