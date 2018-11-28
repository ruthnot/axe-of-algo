#!/usr/bin/python

RED = True
BLACK = False

class Node:
    def __init__(self, key=None, val=None, color=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.color = color


class RedBlackBST:
    def __init__(self):
        self.root = None

    def _is_red(self, x):
        if x == None:
            return False
        return x.color == RED

    def _rotate_left(self, h):
        assert self._is_red(h)
        
