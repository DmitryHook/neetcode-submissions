from math import gcd


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            next_node = curr.next

            gcd_value = gcd(curr.val, next_node.val)
            gcd_node = ListNode(gcd_value)

            curr.next = gcd_node
            gcd_node.next = next_node

            curr = next_node

        return head