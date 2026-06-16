# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            group_end = group_prev
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next

            next_group_start = group_end.next

            prev = next_group_start
            curr = group_prev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            group_start = group_prev.next

            group_prev.next = prev

            group_prev = group_start