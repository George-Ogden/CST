from sys import setrecursionlimit

setrecursionlimit(100000)


def dutch_quicksort(a, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(a)
    if left >= right - 1:
        return
    start = left
    pivot = a[right - 1]
    end = right
    i = start
    while i < end:
        if a[i] < pivot:
            a[i], a[start] = a[start], a[i]
            start += 1
            i += 1
        elif a[i] > pivot:
            end -= 1
            a[i], a[end] = a[end], a[i]
        else:
            i += 1
    dutch_quicksort(a, left, start)
    dutch_quicksort(a, end, right)


def vanilla_quicksort(a, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(a)
    if right - left < 2:
        return
    pivot = partition(a, left, right)
    vanilla_quicksort(a, left, pivot)
    vanilla_quicksort(a, pivot + 1, right)


def partition(a, left, right):
    pivot = right - 1
    right = pivot
    while left < right:
        while left < right and a[left] < a[pivot]:
            left += 1
        while left < right and a[right - 1] >= a[pivot]:
            right -= 1
        if left < right:
            a[left], a[right - 1] = a[right - 1], a[left]
            left += 1
            right -= 1
    a[right], a[pivot] = a[pivot], a[right]
    return right
