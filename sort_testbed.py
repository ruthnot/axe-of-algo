#!/usr/bin/python

from sort_util import SortUtil
from sort_algorithm import MergeSort, QuickSort
from copy import deepcopy
import time

if __name__ == '__main__':
    util = SortUtil()

    arr1 = util.rand_array(1000)
    arr2 = deepcopy(arr1)
    time_1 = time.time()
    MergeSort(arr1)
    time_2 = time.time()
    QuickSort(arr2)
    time_3 = time.time()
    print (time_2 - time_1) * 1000.0
    print (time_3 - time_2) * 1000.0
    # if util.check_sorted(arr):
    #     print "Success"
    #     print time
    # else:
    #     print "Fail"
