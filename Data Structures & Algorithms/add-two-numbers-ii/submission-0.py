# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        result = None
        carry = 0

        while stack1 or stack2 or carry:
            total = carry

            if stack1:
                total += stack1.pop()

            if stack2:
                total += stack2.pop()

            digit = total % 10
            carry = total // 10

            node = ListNode(digit)
            node.next = result
            result = node

        return result