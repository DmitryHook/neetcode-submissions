# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        next_node = curr.next

        first_crit = -1
        prev_crit = -1
        min_dist = float("inf")
        pos = 1

        while next_node:
            if (
                (curr.val > prev.val and curr.val > next_node.val)
                or
                (curr.val < prev.val and curr.val < next_node.val)
            ):
                if first_crit == -1:
                    first_crit = pos

                if prev_crit != -1:
                    dist = pos - prev_crit
                    min_dist = min(min_dist, dist)

                prev_crit = pos

            prev = curr
            curr = next_node
            next_node = next_node.next
            pos += 1

        if first_crit == prev_crit:
            return [-1, -1]

        maximum_dist = prev_crit - first_crit

        return [min_dist, maximum_dist]
