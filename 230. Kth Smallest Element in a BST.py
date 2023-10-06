# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        nodes = []
        nodes = self.inorder_traverse(node, nodes)
        return nodes[k - 1].val
        
    
    def inorder_traverse(self, node, nodes):
        
        if node is None:
            return
        
        self.inorder_traverse(node.left, nodes)
        nodes.append(node)
        self.inorder_traverse(node.right, nodes)

        return nodes
