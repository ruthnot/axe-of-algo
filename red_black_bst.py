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
        assert self._is_red(h.right)
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RED
        return x

    def _rotate_right(self, h):
        assert self._is_red(h.left)
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RED
        return x

    def _flip_colors(self, h):
        assert not self._is_red(h)
        assert self._is_red(h.left)
        assert self._is_red(h.right)
        h.color = RED
        h.left.color = BLACK
        h.left.color = BLACK
        

