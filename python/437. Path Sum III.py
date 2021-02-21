# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0

        res = 0
        stack = [(root, root.val, [root.val])]
        
        while stack:
            curr, curr_sum, path  = stack.pop()
            path_sum = curr_sum
            for val in path:
                if path_sum == sum:
                    res += 1
                path_sum -= val

            if curr.right:
                stack.append((curr.right, curr_sum + curr.right.val, path[:] + [curr.right.val]))
            if curr.left:
                stack.append((curr.left, curr_sum + curr.left.val, path[:] + [curr.left.val]))
        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3
sol = Solution()
print(sol.pathSum(node1, 3))
