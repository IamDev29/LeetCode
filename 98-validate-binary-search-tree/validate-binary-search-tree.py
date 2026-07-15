# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low, high):
            # An empty subtree is perfectly valid
            if not node:
                return True
                
            # Current node value MUST sit strictly inside (low, high) bounds
            if not (low < node.val < high):
                return False
                
            # Going Left: The maximum limit shrinks to node.val
            # Going Right: The minimum limit climbs to node.val
            left_valid = validate(node.left, low, node.val)
            right_valid = validate(node.right, node.val, high)
            
            return left_valid and right_valid
            
        # Launch validation with initial limits set to negative and positive infinity
        return validate(root, float('-inf'), float('inf'))
        