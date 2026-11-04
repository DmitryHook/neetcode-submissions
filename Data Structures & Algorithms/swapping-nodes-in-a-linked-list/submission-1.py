# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first_node = head

        for _ in range(k - 1):
            first_node = first_node.next

        second_node = head
        current = first_node

        while current.next:
            current = current.next
            second_node = second_node.next

        first_node.val, second_node.val = second_node.val, first_node.val

        return head
