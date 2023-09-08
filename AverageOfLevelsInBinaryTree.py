# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def find_average(self, nodes):
        total = 0
        next_level_nodes = []
        for node in nodes:
            total += node.val
            if node.left != None:
                next_level_nodes.append(node.left)
            if node.right != None:
                next_level_nodes.append(node.right)
        
        average = float(total) / len(nodes)

        if len(next_level_nodes) == 0:
            return average, None

        return average, next_level_nodes

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        keepGoing = True
        nodes = [root]
        while keepGoing:
            average, nodes = self.find_average(nodes)
            ans.append(average)

            if nodes is None:
                break
            
        
        return ans

        
