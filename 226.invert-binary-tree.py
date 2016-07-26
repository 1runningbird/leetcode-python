# coding: utf8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    '''
    Google: 90% of our engineers use the software you wrote (Homebrew),
    but you can’t invert a binary tree on a whiteboard so fuck off.
    '''
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root
