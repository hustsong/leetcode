# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node_rec = set()
        
        while headA or headB:
            if headA:
                if id(headA) in node_rec:
                    return headA
                else:
                    node_rec.add(id(headA))
                    headA = headA.next
            if headB:
                if headB in node_rec:
                    return headB
                else:
                    node_rec.add(headB)
                    headB = headB.next

        return None