# coding: utf8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    '''
    The maximum depth is the number of nodes along the
        longest path from the root node down to the farthest leaf node.
    '''
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        num_left = self.maxDepth(root.left)
        num_right = self.maxDepth(root.right)
        return max(num_left, num_right) + 1
