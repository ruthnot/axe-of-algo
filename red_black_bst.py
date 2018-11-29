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

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, h, key, val):
        if h is None:
            return Node(key, val, RED)
        if key < h.key:
            h.left = self._put(h.left, key, val)
        elif key > h.key:
            h.right = self._put(h.right, key, val)
        else:
            h.val = val

        if self._is_red(h.right) and not self._is_red(h.left):
            self._rotate_left(h)
        if self._is_red(h.left) and self._is_red(h.left.left):
            self._rotate_right(h)
        if self._is_red(h.left) and self._is_red(h.right):
            self._flip_colors(h)

        return h

    def get(self, key):
        h = self.root
        while h is not None:
            if key < h.key:
                h = h.left
            elif key > h.key:
                h = h.right
            else:
                return h.val
        return None

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


