import collections
import functools

import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    # TODO - you fill in here.
    
    return []


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


# +
def test_add_interval():
    d = Interval(-4,0)
    n = ([5,6])
    list_interval = [Interval(-4,0), Interval(2,3), Interval(5,6)]
    list_interval
    
test_add_interval()
# -

if __name__ == '__main__':
    generic_test.generic_test_main(
        "interval_add.py",
        'interval_add.tsv',
        add_interval_wrapper,
        res_printer=res_printer)

list_interval = [Interval(-4,0), Interval(2,3), Interval(5,6)]
list_interval[1].left


