# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None: return True

        one, two = head, head.next
        second_head = None
        while True:
            if two.next is None:
                second_head = one.next
                break
            if two.next.next is None:
                second_head = one.next.next
                break
            one = one.next
            two = two.next.next

        # reverse second
        last = None
        node = second_head
        while node:
            next = node.next
            node.next = last
            last = node
            node = next
        second_head = last

        # compare
        while head and second_head:
            if head.val != second_head.val:
                return False
            head = head.next
            second_head = second_head.next

        return True