# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        multiplier = 1
        while l1:
            num1 += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next

        multiplier = 1
        while l2:
            num2 += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next
        

        answer = str(num1 + num2)

        head = ListNode(None)
        curr = head

        for char in answer[::-1]:
            node = ListNode(int(char))
            curr.next = node
            curr = curr.next
        
        return head.next

