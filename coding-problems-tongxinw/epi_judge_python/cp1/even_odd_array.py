import collections
import functools
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A):
    "reorder array A so that Even entries appear first "
    next_even, next_odd = 0, len(A) - 1 
    # next_even is the front index 0, next_odd is the end index len(A)-1; and while looping, front index will add 1 and 
    # move to the right side, end index will minus 1 and move to the left side until they meet.
    while next_even < next_odd: 
        if A[next_even] % 2 == 0: # if the entry is even, then move the next_even to the next index
            next_even += 1
        else:
            # if the entry is odd, then exchange the entries and the next_even and the next_odd index, 
            # so we have odd entries appear at the end of the array, then we move next_odd to the left index to check even or odd
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure("Even elements appear in odd part")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure("Elements mismatch")


if __name__ == '__main__':
    generic_test.generic_test_main("even_odd_array.py",
                                    'even_odd_array.tsv', even_odd_wrapper)
