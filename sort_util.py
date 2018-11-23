#!/usr/bin/python

from random import randint

class SortUtil:
    def __init__(self):
        pass

    @staticmethod
    def rand_array(size=1):
        result = []
        for i in range(int(size)):
            result.append(randint(0, 9))
        return result

    @staticmethod
    def sorted_array(start=0, size=1):
        result = [start]
        for i in xrange(1, int(size)):
            result.append(start + i)
        return result

    @staticmethod
    def check_sorted(arr):
        assert isinstance(arr, list)
        if len(arr) == 1:
            return True
        for i in range(len(arr) - 1):
            if arr[i+1] < arr[i]:
                return False
        return True


if __name__ == '__main__':
    # util = SortUtil()
    # x = util.sorted_array(10)
    # util.check_sorted(x)
    a = [1,2,3,4]
    b = a[0:2]
    print b


