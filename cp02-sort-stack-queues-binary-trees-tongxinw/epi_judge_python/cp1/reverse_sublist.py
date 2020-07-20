import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test

from list_node import ListNode


def reverse_sublist(L, start, finish):
    # TODO - you fill in here.
    return None


if __name__ == '__main__':
    generic_test.generic_test_main("reverse_sublist.py",
                                    "reverse_sublist.tsv", reverse_sublist)
