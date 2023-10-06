# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i in range(len(lists)):
            node = lists[i]
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        
        if not heap:
            return

        head = ListNode(heapq.heappop(heap))
        curr = head
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        
        return head
            

