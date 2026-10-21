# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr_result = result
        curr = head.next
        total = 0

        while curr:
            if curr.val == 0:
                curr_result.next = ListNode(total)
                curr_result = curr_result.next
                total = 0
            else:
                total += curr.val

            curr = curr.next

        return result.next
