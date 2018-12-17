# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        # return self.DFS(root.left, root.right)
        return self.BFS(root)

    def DFS(self, a, b):
        if not a and not b: return True
        if a and b and a.val == b.val:
            return self.DFS(a.left, b.right) and self.DFS(a.right, b.left)
        else:
            return False

    def BFS(self, root):
        if not root: return True
        q = deque()
        q.append(root.left)
        q.append(root.right)

        while len(q) > 1:
            if (q[0] and not q[1]) or (not q[0] and q[1]):
                return False
            elif q[0] and q[1] and q[0].val != q[1].val:
                return False
            else:
                if q[0] and q[1]:
                    q.append(q[0].left)
                    q.append(q[1].right)
                    q.append(q[0].right)
                    q.append(q[1].left)
                q.popleft()
                q.popleft()
        return True
