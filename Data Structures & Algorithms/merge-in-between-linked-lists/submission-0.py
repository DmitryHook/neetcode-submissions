# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:
        node_before = list1

        for _ in range(a - 1):
            node_before = node_before.next

        node_after = node_before

        for _ in range(b - a + 2):
            node_after = node_after.next

        list2_tail = list2

        while list2_tail.next:
            list2_tail = list2_tail.next

        node_before.next = list2
        list2_tail.next = node_after

        return list1
