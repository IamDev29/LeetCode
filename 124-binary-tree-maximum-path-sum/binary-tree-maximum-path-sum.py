# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxi=float('-inf')
        def maxSum(root):
        
            if root is None:
                return 0

            leftsum=max(0,maxSum(root.left))
            rightsum=max(0,maxSum(root.right))
            self.maxi=max(self.maxi,leftsum+rightsum+root.val)

            return (root.val)+max(leftsum,rightsum)

        maxSum(root)
        return self.maxi

        
        