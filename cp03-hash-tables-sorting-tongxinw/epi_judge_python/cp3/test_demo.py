# #
#  Example cp3.1 heap sort testing setup.
# #
# This files includes some test functions and some
# example sorting functions that you can try it out on.
# When you are ready to use it on your
# own code, uncomment the lines in the TODO section below.
#
# USAGE: You can run all the tests by running this file as
# from the terminal via
#
# python test_heap_sort.py
#
# And also via pytest via
#
# pytest -v test_heap_sort.py
#
# Included Examples:
#
# heap_sort_ex
# heap_sort_ex is a a very inefficient heap sort example
# based on the BinHeap.pu stencil code.
# It does not operate inplace. It does not provide a stable sort.
#
# builtin_sort
# builtin_sort uses list.sort() and passes all tests.
# It operates inplace and provides a stable sort.

# from BinHeap import BinHeap
import pytest
import sys

# def heap_sort_ex(L, key=None):
#     '''Returns a shallow copy of L in *descending* order.  This is an unstable sort.
#        [Not Implemented]: When a key function is supplied, the key values determine the sort
# order.
#        Time complexity is O(n). Space complexity is O(n).'''
#     bh = BinHeap()
#     bh.buildHeap(L)
#     R = []
#     for _ in range(len(L)):
#         R.insert(0, bh.delMin())
#     return R
#
#
# def builtin_sort(L, key=None):
#     '''Wrapper of builtin Python sort method.
#        Creates a stable sort on L inplace, and in *descending* order. Also returns L.
#        Normally, list.sort() will L inplace in *ascending* order, but here the reverse flag
#        is used to change it to *descending* order.
#        Time complexity is O(n log n), Space Complexity is O(1).'''
#     L.sort(key=key, reverse=True)
#     return L
#
#
# sorts_to_check = [heap_sort_ex, builtin_sort]


# TODO:
# Uncomment the following to three lines to run these tests
# on your problem solutions: (your sort function signatures should
# match heap_sort_ex's signature.)


from heap_sort import heap_sort
from heap_sort import heap_sort_stable

sorts_to_check = [heap_sort, heap_sort_stable]

# Begin Testing
LL = [[], [1], [2, 1], [1, 2], [3, 2, 1], [1, 2, 3], [1, 3, 2]]


@pytest.mark.parametrize("sort", sorts_to_check)
@pytest.mark.timeout(1)
def test_sort(sort):
    """ input array should be sorted """
    for L in LL:
        Lcopy = L.copy()
        R = sort(Lcopy)
        assert R == sorted(L, reverse=True), 'sort order is correct'


@pytest.mark.parametrize("sort", sorts_to_check)
@pytest.mark.timeout(1)
def test_inplace(sort):
    """ heap sort functions should return the input array instead of a copy """
    for L in LL:
        Lcopy = L.copy()
        R = sort(Lcopy)
        assert id(R) == id(Lcopy), 'sort is in place'


stableLL = [[(0, 'is'), (0, 'it'), (1, 'sta'), (1, 'ble'), (2, '?')],
            [(4, 'llll'), (7, 'ex'), (3, 'le'), (7, 'el'), (3, 'nt')]]


@pytest.mark.timeout(1)
def test_stable():
    """ `heap_sort_stable` should be stable """
    for L in stableLL:
        Lcopy = L.copy()
        R = heap_sort_stable(Lcopy, key=lambda x: x[0])
        assert R == sorted(L, key=lambda x: x[0], reverse=True), 'sort is stable'


if __name__ == '__main__':
    # Run tests in this file
    cmd = f'--verbose --showlocals {sys.argv[0]} '
    # uncomment cmd+= to include coverage info
    cmd += '--cov-report=html --cov-report=term --cov=.'
    pytest.main(cmd.split())
