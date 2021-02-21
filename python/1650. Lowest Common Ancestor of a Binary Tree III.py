"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_l, q_l = 0, 0

        p_ref = p
        while p_ref.parent:
            p_ref = p_ref.parent
            p_l += 1
        q_ref = q
        while q_ref.parent:
            q_ref = q_ref.parent
            q_l += 1

        if q_l != p_l:
            node = p if p_l > q_l else q
            for _ in range(abs(q_l - p_l)):
                if node.parent:
                    node = node.parent
            if p_l > q_l:
                p = node
            else:
                q = node
        q_l = p_l = min(q_l, p_l)

        while q_l >= 0:
            if q == p:
                return q
            if q.parent:
                q = q.parent
            if p.parent:
                p = p.parent
            q_l -= 1
            