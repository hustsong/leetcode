# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def minDiffInBST(self, root: TreeNode) -> int:
    #     L = []
    #     def dfs(node):
    #         if node.left: dfs(node.left)
    #         L.append(node.val)
    #         if node.right: dfs(node.right)
        
    #     dfs(root)
    #     return min([b - a for a, b in zip(L, L[1:])])

    def minDiffInBST(self, root: TreeNode) -> int:
        L, stack = [], []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            L.append(curr.val)
            curr = curr.right

        return min([b - a for a, b in zip(L, L[1:])])

