#!/usr/bin/python

from sort_util import SortUtil
from copy import deepcopy
import math


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



