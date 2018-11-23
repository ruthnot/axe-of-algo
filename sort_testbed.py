#!/usr/bin/python

from sort_util import SortUtil
from sort_algorithm import MergeSort


if __name__ == '__main__':
    util = SortUtil()

    arr = util.rand_array(10)
    print arr
    merge_sort = MergeSort(arr)
    if util.check_sorted(arr):
        print "Success"
    else:
        print "Fail"
    print arr
