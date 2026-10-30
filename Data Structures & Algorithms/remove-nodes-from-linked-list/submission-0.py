# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        dummy = ListNode(0)
        tail = dummy
        max_val = 0
        curr = prev
        
        while curr:
            if curr.val >= max_val:
                max_val = curr.val
                tail.next = curr
                tail = curr
            curr = curr.next
        tail.next = None

        prev = None
        curr = dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
