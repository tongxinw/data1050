import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test
from list_node import ListNode


def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    """
    Inputs are two head ListNode instances of linked lists of integers; 
    output is a ListNode instance - the head of the combined sorted linked list.
    Time Complexity: O(m+n) where m is the length of L1 and n is the length of L2
    Space Complexity: O(3) which is just O(1)

    """
    new_head = ListNode()
    p = new_head
    new_tail = ListNode()
    new_head.next = new_tail
    while L1 and L2:
        if L1.data <= L2.data:
            new_tail.next = ListNode(L1.data)
            L1 = L1.next
        else:
            new_tail.next = ListNode(L2.data)
            L2 = L2.next
        new_tail = new_tail.next
    
    if L1:
        new_tail.next = L1
    elif L2:
        new_tail.next = L2
        
    return new_head.next.next



if __name__ == '__main__':
    generic_test.generic_test_main("sorted_lists_merge.py",
                                   'sorted_lists_merge.tsv',
                                   merge_two_sorted_lists)

node1 = ListNode(5)
node1.next = ListNode(13)
node1.next.next = ListNode(17)
node1


