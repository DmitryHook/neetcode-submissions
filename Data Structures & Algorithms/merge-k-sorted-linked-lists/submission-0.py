# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        min_heap = []

        for node in lists:
            if node:
                heapq.heappush(min_heap, NodeWrapper(node))
        
        while min_heap:
            wrapper = heapq.heappop(min_heap)
            node = wrapper.node

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(min_heap, NodeWrapper(node.next))

        return dummy.next