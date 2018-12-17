# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.compare(root.left, root.right)

    def compare(self, a, b):
        if not a and not b: return True
        if a and b and a.val == b.val:
            return self.compare(a.left, b.right) and self.compare(a.right, b.left)
        else:
            return False

