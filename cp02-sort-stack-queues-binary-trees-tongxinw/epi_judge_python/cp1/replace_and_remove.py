import functools
import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    # TODO - you fill in here.
    return 0


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    generic_test.generic_test_main("replace_and_remove.py",
                                   'replace_and_remove.tsv',
                                   replace_and_remove_wrapper)
