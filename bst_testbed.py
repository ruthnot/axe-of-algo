#!/usr/bin/python
from binary_search_tree import BST

if __name__ == '__main__':
    t = BST()
    t.put(1, 1)
    t.put(3, 3)
    t.put(2, 2)
    print t.size()

