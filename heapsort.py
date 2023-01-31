import random


def heapify(a, root_index, end_index):
    mx = root_index
    for child in [root_index * 2 + 1, root_index * 2 + 2]:
        if child < end_index and a[child] > a[mx]:
            mx = child
    if mx == root_index:
        return a
    a[root_index], a[mx] = a[mx], a[root_index]
    heapify(a, mx, end_index)


def heapsort(a):
    for k in reversed(range(len(a) // 2)):
        heapify(a, k, len(a))

    for k in reversed(range(1, len(a))):
        a[0], a[k] = a[k], a[0]
        heapify(a, 0, k)
