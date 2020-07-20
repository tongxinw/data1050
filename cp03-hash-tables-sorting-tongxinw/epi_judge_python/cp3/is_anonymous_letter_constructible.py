import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    """
    Inputs are the note and magazine text; 
    output is boolean indicating whether it is possible to write an anonymous letter using the magazine
    
    Time Complexity: O(m+l) where m is the length of magazine_text and l is the length of letter_text
    Space Complexity: O(m+l)
    """
#     import string
    l = list(letter_text)
    m = list(magazine_text) 
    d_m = {}
    # assume dict is O(1) look up
    for char in m:
        if char not in d_m:
            d_m[char] = 1
        else:
            d_m[char] += 1
    
    for char in l:
        if char not in d_m:
            return False
        else:
            d_m[char] -= 1
            if d_m[char] < 0:
                return False
    return True


# +
def test_is_letter_constructible_from_magazine():
    letter_text1 = "abc"
    magazine_text1 = "abc"
    assert is_letter_constructible_from_magazine(letter_text1, magazine_text1) == True
    
    letter_text2 = "abbc"
    magazine_text2 = "abc"
    assert is_letter_constructible_from_magazine(letter_text2, magazine_text2) == False
    
    letter_text3 = ""
    magazine_text3 = "abc"
    assert is_letter_constructible_from_magazine(letter_text3, magazine_text3) == True
    
    letter_text4 = ""
    magazine_text4 = ""
    assert is_letter_constructible_from_magazine(letter_text4, magazine_text4) == True
    
    letter_text5 = "abc"
    magazine_text5 = ""
    assert is_letter_constructible_from_magazine(letter_text5, magazine_text5) == False
    
    letter_text6 = "Aabc"
    magazine_text6 = "aabc"
    assert is_letter_constructible_from_magazine(letter_text5, magazine_text5) == False
    
    print("PASS!")
    
test_is_letter_constructible_from_magazine()
# -

if __name__ == '__main__':
    generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                   'is_anonymous_letter_constructible.tsv',
                                   is_letter_constructible_from_magazine)
