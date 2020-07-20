import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    return 0.0


if __name__ == '__main__':
    generic_test.generic_test_main("buy_and_sell_stock.py",
                                   "buy_and_sell_stock.tsv",
                                   buy_and_sell_stock_once)
