import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    """
    This function takes an array of daily stock prices(which is prices),
    and returns the maximum profit that could be made by buying and then selling one share of that
    stock within the time window specified. 
    Return 0 if no profit is possible
    """
    low = prices[0]
    maxProfit = 0
    for price in prices:
        if price < low:
            low = price
        elif price - low > maxProfit:
            maxProfit = price - low
    return maxProfit


def test_buy_and_sell_stock_once():
    prices1 = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    prices2 = [5,0,0,0,0]
    print(buy_and_sell_stock_once(prices1))
    print(buy_and_sell_stock_once(prices2))
test_buy_and_sell_stock_once()

if __name__ == '__main__':
    generic_test.generic_test_main("buy_and_sell_stock.py",
                                   "buy_and_sell_stock.tsv",
                                   buy_and_sell_stock_once)
