#!/usr/bin/python

from sort_util import SortUtil
from copy import deepcopy
import random
import math

from priority_queue import MaxHeap


class MergeSort:
    def __init__(self, arr):
        aux = deepcopy(arr)
        self._sub_sort(arr, aux, 0, len(arr) - 1)

    def _merge(self, arr, aux, lo, mid, hi):
        assert SortUtil.check_sorted(arr[lo:mid + 1])
        assert SortUtil.check_sorted(arr[mid + 1:hi + 1])
        aux[lo:hi + 1] = arr[lo:hi + 1]
        i = lo
        j = mid + 1
        for k in xrange(lo, hi + 1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > hi:
                arr[k] = aux[i]
                i += 1
            elif aux[i] <= aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1

    def _sub_sort(self, arr, aux, lo, hi):
        if lo >= hi:
            return
        mid = int(math.floor(lo + (hi - lo) / 2.0))
        self._sub_sort(arr, aux, lo, mid)
        self._sub_sort(arr, aux, mid + 1, hi)
        self._merge(arr, aux, lo, mid, hi)


class QuickSort:
    def __init__(self, arr):
        random.shuffle(arr)
        self.c = 0
        self._sub_sort(arr, 0, len(arr)-1)

    def _partition(self, arr, lo, hi):
        self.c += 1
        i = lo + 1
        j = hi
        while True:
            while arr[i] < arr[lo]:
                i += 1
                if i >= hi:
                    break
            while arr[j] > arr[lo]:
                j -= 1
                if j <= lo:
                    break
            if i >= j:
                break
            self._exchange(arr, i, j)
            i += 1
            j -= 1
        self._exchange(arr, lo, j)
        return j

    def _sub_sort(self, arr, lo, hi):
        if lo >= hi:
            return
        j = self._partition(arr, lo, hi)
        self._sub_sort(arr, lo, j-1)
        self._sub_sort(arr, j+1, hi)

    def _exchange(self, arr, x, y):
        _aux = deepcopy(arr[x])
        arr[x] = arr[y]
        arr[y] = _aux


class HeapSort:
    def __init__(self, arr):
        self._sort(arr)

    def _sort(self, arr):
        _res = []
        heap = MaxHeap(arr)
        for k in range((len(heap.arr)-1)/2, 0, -1):
            heap.sink(k)
        while len(heap.arr) > 1:
            _res.insert(0, heap.del_max())
        for i in range(len(arr)):
            arr[i] = _res[i]




