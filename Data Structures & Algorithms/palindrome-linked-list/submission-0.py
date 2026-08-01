# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        left, right = head, prev
        is_palindrome = True

        while right:
            if left.val != right.val:
                is_palindrome = False
                break
            left = left.next
            right = right.next

        return is_palindrome