# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None 

        # recursively sort the left and right, ie merge sort
        left = self.sortList(head)
        right = self.sortList(mid)

        curr = ListNode(0)
        head = curr
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        else:
            curr.next = right
        
        return head.next
