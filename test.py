#!/usr/bin/python

from collections import deque

if __name__=='__main__':
    q = deque()
    q.append(1)
    q.append(None)
    q.popleft()
    print q
    print len(q)
    print q[0] is None



