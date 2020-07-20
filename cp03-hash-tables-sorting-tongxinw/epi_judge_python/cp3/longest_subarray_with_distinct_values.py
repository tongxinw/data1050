import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


# +
def longest_subarray_with_distinct_entries(A):
    # TODO - you fill in here.
    
    """ Input is an array; output is an int that represents the length of a longest subarray with property 
        that all its elements are distinct.

        The time complexity is O(n)
        the spsce complexity is O(n)
    """
    
    begin = -1
    maxL = 0
    dic = {}
    
    for i, char in enumerate(A):
        if char in dic and dic[char] > begin:
            begin = dic[char]
            dic[char] = i
        else:
            dic[char] = i
            if i - begin > maxL:
                maxL = i - begin
    return maxL



#     latest_ind = {} # store the lastest index less than the current index that holding the same value
#     logst_start_ind = 0
#     output = 0
#     for i, char in enumerate(A):
#         if char in latest_ind:
#             tmp = latest_ind[char] # update tmp index that keep track of duplicate index
#             if tmp >= logst_start_ind: # catch duplicate
#                 if output < i - logst_start_ind:
#                     output  = i - logst_start_ind # update longest length
#                 logst_start_ind = tmp + 1 # otherwise, cut and go to next index to check longest
#         latest_ind[char] = i 
#     return max(output, len(A) - logst_start_ind)
# -


def test_longest_subarray_with_distinct_entries():
    A = "abcdeabc"
    B = "f,s,f,e,t,w,e,n,w"
    print(longest_subarray_with_distinct_entries(A))
    print(longest_subarray_with_distinct_entries(B))
test_longest_subarray_with_distinct_entries()    

if __name__ == '__main__':
    generic_test.generic_test_main(
        "longest_subarray_with_distinct_values.py",
        'longest_subarray_with_distinct_values.tsv',
        longest_subarray_with_distinct_entries)


