import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


class BinaryTreeNode :
    def __init__ (self, data = None , left = None , right = None ):
        self.data = data
        self.left = left
        self.right = right


def sum_root_to_leaf(tree, partial_path_sum=0):
    # TODO - you fill in here.
    """
    Inputs are the root of a binary tree and the sum from root to leaf that is 0 
    by default; output is the sum of the binary numbers represented 
    by the root-to-leaf paths.
    """
    if not tree:
        return False
    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:
        return partial_path_sum
    else:
        partial_path_sum = sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(tree.right, partial_path_sum)
        return partial_path_sum


def test_sum():
    n1 = BinaryTreeNode(1, None, None)
    n2 = BinaryTreeNode(0, n1, None)
    n5 = BinaryTreeNode(1, None, None)
    n4 = BinaryTreeNode(0, None, n5)
    n3 = BinaryTreeNode(1, n2, n4)
    assert sum_root_to_leaf(n3) == 10
    n6 = BinaryTreeNode(0, None, None)
    n7 = BinaryTreeNode(1, None, None)
    n8 = BinaryTreeNode(1, n6,n7)
    assert sum_root_to_leaf(n8) == 5
    
    print("All tests pass!")
test_sum()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sum_root_to_leaf.py", 'sum_root_to_leaf.tsv', sum_root_to_leaf))
