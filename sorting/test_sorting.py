import random

from quicksort import dutch_quicksort, vanilla_quicksort
from heapsort import heapsort


def test_dutch_quicksort_on_empty_list():
    a = []
    dutch_quicksort(a)
    assert a == []


def test_vanilla_quicksort_on_empty_list():
    a = []
    vanilla_quicksort(a)
    assert a == []


def test_heapsort_on_empty_list():
    a = []
    heapsort(a)
    assert a == []


def sorting_test(sorting_algorithm):
    for _ in range(1000):
        n = random.randint(1, 20)
        a = [random.randint(1, 20) for _ in range(n)]
        expected = list(sorted(a))
        sorting_algorithm(a)
        assert a == expected


def test_dutch_quicksort_random():
    sorting_test(dutch_quicksort)


def test_vanilla_quicksort_random():
    sorting_test(vanilla_quicksort)


def test_heapsort_random():
    sorting_test(heapsort)


def test_dutch_equality():
    x = [2] * 100_000
    dutch_quicksort(x)
    assert x == [2] * 100_000


def test_vanilla_equality():
    x = [2] * 10_000
    vanilla_quicksort(x, 0, len(x))
    assert x == [2] * 10_000
