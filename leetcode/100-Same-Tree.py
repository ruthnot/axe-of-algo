# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        que = deque()
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            que.extend([p.left, q.left, p.right, q.right])
            while len(que) >= 2:
                if que[0] and que[1]:
                    if que[0].val != que[1].val:
                        return False
                    else:
                        que.extend([que[0].left,  que[1].left, que[0].right, que[1].right])
                elif (que[0] and not que[1]) or (que[1] and not que[0]):
                    return False
                que.popleft()
                que.popleft()
            return True
        else:
            return False
