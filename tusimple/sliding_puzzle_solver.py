#! /usr/bin/python

from copy import deepcopy


class SlidingPuzzle:
    def __init__(self):
        pass

    def solve(self, board):
        # change to list
        arr = list()
        for row in board:
            for num in row:
                arr.append(num)
        # queue: arr, operation, index of x
        q = list()
        first_node = {'arr': arr, 'ops': [None], 'x_idx': arr.index(0)}
        q.append(first_node)
        # if marked
        marked = list()
        while q:
            target_node = q[0]
            if target_node['arr'] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
                return target_node['ops'][1:]
            if target_node['arr'] not in marked:
                for op in self._operations(target_node['x_idx']):
                    new_node = deepcopy(target_node)
                    swap_idx = self._get_swap_idx(target_node['x_idx'], op)
                    new_node['arr'][swap_idx] = target_node['arr'][target_node['x_idx']]
                    new_node['arr'][target_node['x_idx']] = target_node['arr'][swap_idx]
                    new_node['ops'].append(op)
                    new_node['x_idx'] = swap_idx
                    q.append(new_node)
                    marked.append(target_node['arr'])
            q.pop(0)
        return -1

    def _operations(self, idx):
        if idx == 0:
            return [1, 2]
        elif idx == 3:
            return [2, 3]
        elif idx == 12:
            return [0, 1]
        elif idx == 15:
            return [0, 3]
        elif idx == 1 or idx == 2:
            return [1, 2, 3]
        elif idx == 4 or idx == 8:
            return [0, 1, 2]
        elif idx == 7 or idx == 11:
            return [0, 2, 3]
        elif idx == 13 or idx == 14:
            return [0, 1, 3]
        else:
            return [0, 1, 2, 3]

    def _get_swap_idx(self, idx, operation):
        if operation == 0:
            return idx - 4
        elif operation == 1:
            return idx + 1
        elif operation == 2:
            return idx + 4
        elif operation == 3:
            return idx - 1
        else:
            raise NameError('error')


if __name__ == '__main__':
    board = [[1, 2, 3, 4], [5, 6, 7, 0], [9, 10, 11, 8], [13, 14, 15, 12]]
    board2 = [[4, 11, 15, 1], [8, 9, 10, 2], [3, 13, 0, 12], [6, 7, 5, 14]]
    _ = SlidingPuzzle()
    print _.solve(board)
