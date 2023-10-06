# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = [1]
        stackB = [2]

        nodeA = headA
        nodeB = headB

        while nodeA or nodeB:
            if nodeA:
                stackA.append(nodeA)
                nodeA = nodeA.next
            
            if nodeB:
                stackB.append(nodeB)
                nodeB = nodeB.next

        prev = None

        while stackA and stackB:
            nodeA = stackA.pop()
            nodeB = stackB.pop()

            if nodeA != nodeB:
                return prev
            
            prev = nodeA
            
            
        

        
