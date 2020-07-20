import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


def is_well_formed(s):
    """
        Input s is a string made up of characters (, ) ,[ ,], { and };
        output is a boolean whether parentheses match and in the correct order.
    """
    # TODO - you fill in here.
    s = list(s)
    op = []
    l = len(s)
    for i in range(l):
        if s[i] in ['(','{','[']:
            op.append(s[i])
        else: 
            if len(op) == 0:
                return False
            temp = op.pop() 
            if s[i] == ')':
                if temp != '(':
                    return False
            elif s[i] == '}':
                if temp != '{':
                    return False
            else:
                if temp != '[':
                    return False
    if len(op) != 0:
        return False
    return True


def test_is_well_formed():
    assert is_well_formed("({[]})") == True
    assert is_well_formed("(") == False
    assert is_well_formed(")(") == False
    assert is_well_formed("({[})") == False
    print("All tests pass!")
test_is_well_formed()

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
