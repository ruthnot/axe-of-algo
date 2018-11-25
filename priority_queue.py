#!/usr/bin/python

from copy import deepcopy


class MaxHeap:
    def __init__(self, arr=list()):
        self.arr = deepcopy(arr)
        if len(self.arr) == 0 or self.arr[0] is not None:
            self.arr = [None] + self.arr

    def insert(self, v):
        self.arr.append(v)
        self.swim(len(self.arr)-1)

    def del_max(self):
        v_max = self.arr[1]
        self._exchange(1, len(self.arr)-1)
        self.arr.pop()
        self.sink(1)
        return v_max

    def is_empty(self):
        pass

    def swim(self, k):
        while k > 1 and self.arr[k] > self.arr[k/2]:
            self._exchange(k, k/2)
            k = k/2

    def sink(self, k):
        while 2*k < len(self.arr):
            j = 2*k
            if 2*k+1 < len(self.arr) and self.arr[2*k] < self.arr[2*k+1]:
                j = 2*k+1
            if self.arr[j] <= self.arr[k]:
                break
            self._exchange(k, j)
            k = j

    def _exchange(self, k1, k2):
        _hold = deepcopy(self.arr[k1])
        self.arr[k1] = self.arr[k2]
        self.arr[k2] = _hold

    def check_max_heap(self):
        size = len(self.arr)
        for k in xrange(1, size):
            k_l = False if (2*k) < size and self.arr[2*k] > self.arr[k] else True
            k_r = False if (2*k+1) < size and self.arr[2*k+1] > self.arr[k] else True
            if not (k_l and k_r):
                return False
        return True


if __name__ == "__main__":
    a = [30, 27, 23, 17, 16, 15, 13, 14, 18, 11]
    b = []
    x = MaxHeap()
    # r = x.del_max()
    # print str(r) + " is deleted"
    # print x.arr
    # res = x.check_max_heap()
    #
    # # print res
    # for i in range(10, 0, -1):
    #     print i