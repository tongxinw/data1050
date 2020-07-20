import functools
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    """
    This function rearranges the elements of its input array A such that all elements less than 
    A[pivot_index] (the "pivot") appear first, followed by elements equal to the pivot, 
    followed by elements greater than the pivot.
    """
    pivot = A[pivot_index]
    front, end = 0, len(A) - 1
    
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[front] = A[front], A[i]
            front += 1
    
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[end] = A[end], A[i]
            end -= 1
    return A


def test_dutch_flag_partition():
    A = [1,2,2,1,3]
    print(dutch_flag_partition(0, A))
    B = [0]
    print(dutch_flag_partition(0, B))
    C = [1,2,3,1,3]
    print(dutch_flag_partition(1, C))
test_dutch_flag_partition()


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    generic_test.generic_test_main("dutch_national_flag.py",
                                   'dutch_national_flag.tsv',
                                   dutch_flag_partition_wrapper)
