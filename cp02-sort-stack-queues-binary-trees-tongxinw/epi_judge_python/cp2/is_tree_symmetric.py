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


def is_symmetric(tree):
    # TODO - you fill in here.
    """
    A binary tree is symmetric if you can draw a vertical line through the root and then the left
    subtree is the mirror image of the right subtree. Input a tree and return true if the binary 
    tree is symmetric, return false if it is not. 
    """
    def check(subtree_l, subtree_r):
        if not subtree_l and not subtree_r:
            return True
        elif not subtree_l or not subtree_r:
            return False
        else:
            if subtree_l.data == subtree_r.data:
                if check(subtree_l.left, subtree_r.right) and check(subtree_l.right, subtree_r.left):
                    return True
                else:
                    return False
            else:
                return False
    return not tree or check(tree.left, tree.right)


def test_sym():
    n1 = BinaryTreeNode(1, None, None)
    n2 = BinaryTreeNode(0, n1, None)
    n5 = BinaryTreeNode(1, None, None)
    n4 = BinaryTreeNode(0, None, n5)
    n3 = BinaryTreeNode(1, n2, n4)
    assert is_symmetric(n3)
    n6 = BinaryTreeNode(1, None, None)
    n7 = BinaryTreeNode(1, None, None)
    n8 = BinaryTreeNode(1, n6,n7)
    assert is_symmetric(n8)
    print("All tests pass!")
test_sym()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
