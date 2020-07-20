import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    """
    Input is an array of strings; output is int representing the distance between 
    the closest pair of equal entries.
    
    Time Complexity: O(n) where n is the length of paragraph 
    Space Complexity: The worst case space complexity is O(n + n) where n is the length of the paragraph,
    and on average it is O(n)
    """
    
    #because dictionary is O(1) look-up
    #better way to do: min to store the value instead of a list
    dic = {}
    distance_count = []
    if len(paragraph) <= 1:
        return -1
    else:
        for i in range(len(paragraph)):
            if paragraph[i] not in dic:
                dic[paragraph[i]] = i
            else:
                distance_count.append(i - dic.get(paragraph[i]))
                dic[paragraph[i]] = i
        if distance_count:
            return min(distance_count)
        else:
            return -1


def test_find_nearest_repetition():
    
    l1 = []
    assert find_nearest_repetition(l1) == -1
    l2 = ["a"]
    assert find_nearest_repetition(l2) == -1
    l3 = ["All", "work", "all", "no", "no"]
    assert find_nearest_repetition(l3) == 1
    l4 = ["All", "work", "all", "no", "hello", "hi", "I", "i"]
    assert find_nearest_repetition(l4) == -1
    l5 = ["a", "A"]
    assert find_nearest_repetition(l5) == -1
    
    print("Yeah!!! All tests pass!!!!")
test_find_nearest_repetition()

if __name__ == '__main__':
    generic_test.generic_test_main("nearest_repeated_entries.py",
                                   'nearest_repeated_entries.tsv',
                                   find_nearest_repetition)
