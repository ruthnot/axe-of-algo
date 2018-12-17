#!/usr/bin/python

from collections import deque

if __name__=='__main__':
    q = deque()

    q.extend([1,2,3])
    q.append(None)
    q.popleft([0,1])
    print q
    print len(q)
    print q[0] is None



