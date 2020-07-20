import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


def is_palindrome(s):
    """
    A palindromic string is one that reads the same when it is reversed. 
    This function returns whether an input string s is palindromic ignoring punctuation.
    """
    i,j = 0, len(s)-1
    while i < j:
        while s[i].isalnum() == False:
            i += 1
        while s[j].isalnum() == False:
            j -= 1
        if s[i].upper() == s[j].upper():
            i += 1
            j -= 1
        else:
            return False
    return True


def test():
    s1 = "123.321"
    s2 = "12.3.431!"
    s3 = "%"
    s4 = "aha"
    s5 = "ah2222222ha!"
    s6 = ""
    s7 = "ahA"
    s8 = "ah^A"
    s = [s1, s2, s3, s4, s5, s6, s7, s8]
    for s_arr in s:
        print(is_palindrome(s_arr))
test()

if __name__ == '__main__':
    generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                   "is_string_palindromic_punctuation.tsv",
                                   is_palindrome)
