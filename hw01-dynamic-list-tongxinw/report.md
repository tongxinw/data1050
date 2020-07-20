# DynamicList Report

Banner ID:  

-----

## Q1.1

When we extend the capacity by one element, the amortized time complexity is O(n) as we create a new array and copy every element in the old one. So when we extend the capacity m times, the amortized time complexity is m*O(n); When we increase the capacity by k, the amortized time complexity is O(1), and will be O(n) only when we expand the capacity, so the total amortized time complexity is 0(1) + O(1) + ..+ O(n) + O(1) + O(1) + ... + O(n) < m*O(n) 

## Q1.2

If we shrink the dynamic array to capacity C/K when the length is less than C/K, when we append/insert one element in the array, we will need to expand the capacity again and copy the whole array immediately. If we wait until the length is less than C/(2K), we are reducing the amortized time complexity of expanding the array if we append/insert right after the length becomes C/K. 

## Q1.3
Q1.3 In your report, describe what tests you have created.
a. test_insert()
This method tests inserting an element at index 0,1,...; it also tests inserting an element out of the index range.
b. test_pop()
This method tests deleting the element at index i and returns it; I tested by pop out all the elements in an array.
c. test_reverse()
This method reverses the orignal array. I tested it by appending elements into the array and reversing it. 

## Q1.4
Q1.4 List the typical and worst-case time complexity of each DynamicArray method. In order to do this, for each method you should describe a typical case and worst case. Note: Q1.5 will ask you about average complexity.
a. append()
The typical case would be only increase the capacity by a factor K when necessary. The worst case would be increase the capacity by one everytime the append() function gets executed. 
b. insert()
The typical case would be shifting the elements after the index to the right by 1, and increase the capacity only a factor K. The worst case would be increase the capacity by 1 and copy the whole array, and then insert the element into the new array by shifting other elements to the right by 1. 
c. pop()
The typical case would be shrink the capacity only when the length is less than capacity/2K, and shift the elements after the location index to the lefe by 1. The worst case would be shrinking the array by 1 everytime the pop() function gets executed, and copy all the elements. 
d. reverse()
The typical case would be reverse the two elements with corresponding index(same distances to the middle of the array) without creating a new array; The worst case would be creating a new array and copy every element to their corresponding index. 

## Q1.5
Q1.5 What is the average complexity ("amortized time") of append and why? In other words, if the list grows from 1 to N, how many copy operations will be required, on average, per call to append? Show your calculation and write your final answer in Big-O format.

2^2 + 2^3 + 2^4 + ... + 2^n = N
solve for n, n = log2((N+2)/2+1)
avg = O(N/(log2((N+2)/2+1))-2)
