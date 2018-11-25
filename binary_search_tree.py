#!/usr/bin/python


class Node:
    def __init__(self, key=None, val=None, count=0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = count


class BST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, x):
        if x is None:
            return 0
        return x.count

    def rank(self, key):
        return self._rank(key, self.root)

    def _rank(self, key, x):
        if x is None:
            return 0
        if key < x.key:
            return self._rank(key, x.left)
        elif key > x.key:
            return 1 + self._size(x.left) +  self._rank(key, x.right)
        else:
            return self._size(x.left)

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, x, key, val):
        if x is None:
            return Node(key, val, 1)
        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.count = 1 + self._size(x.left) + self._size(x.right)
        return x

    def get(self, key):
        x = self.root
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None

    def floor(self, key):
        x = self._floor(self.root, key)
        if x is None:
            return None
        return x.key

    def _floor(self, x, key):
        if x is None:
            return None
        if x.key == key:
            return x
        if x.key > key:
            return self._floor(x.left, key)

        t = self._floor(x.right, key)
        if t is not None:
            return t
        else:
            return x

    def max_key(self):
        x = self.root
        if x is None:
            return None
        while x.right is not None:
            x = x.right
        return x.key

    def min_key(self):
        x = self.root
        if x is None:
            return None
        while x.left is not None:
            x = x.left
        return x.key
