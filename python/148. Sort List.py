# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def merge_sort(head: ListNode):
            if head is None or head.next is None:
                return head

            # get pivot



            # merge
            


        return merge_sort(head)

