def insertion_sort_rec(a):
    n = len(a)
    def insertionSortRecursive(arr,n): 
    # base case 
        if n<=1: 
            return
      
    # Sort first n-1 elements 
        insertionSortRecursive(arr,n-1) 
        '''Insert last element at its correct position 
            in sorted array.'''
        last = arr[n-1] 
        j = n-2

          # Move elements of arr[0..i-1], that are 
          # greater than key, to one position ahead 
          # of their current position  
        while (j>=0 and arr[j]>last): 
            arr[j+1] = arr[j] 
            j = j-1

        arr[j+1]=last
    insertionSortRecursive(a,n)
    return a


def test_insertion_sort_rec():
    assert insertion_sort_rec([]) == []
    assert insertion_sort_rec([1]) == [1]
    assert insertion_sort_rec([6,5,3,1,8,7,2,4]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert insertion_sort_rec([0,0]) == [0,0]
    print("All tests pass!")
test_insertion_sort_rec()
