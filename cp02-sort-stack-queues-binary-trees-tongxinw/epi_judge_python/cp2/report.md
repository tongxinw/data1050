
## Insertion Sort (CP2.1)
C) Come up with a worst case Algorithmic Runtime (ART).      
The worst case would be the input is a descending list, then the algorithmic runtime would be $O(n^2)$ since for each element j, it will scan and switch with the entire list before it. 


D) Determine and formally prove the algorithm’s worst case time complexity.  State the nature of the worst case input.      

For a list of length n, the worst case time complexity $T(n) = 1 + 2 + \cdots + (n-1) = \frac{1}{2}n(n-1)$, and for $c = \frac{1}{2}$, $n_{0} = 1$, $\frac{1}{2}n(n-1) \leq \frac{1}{2}n^2$ for all $n \geq 1$, thus the worst case time complexity is $O(n^2)$. The worst case input would be a descending list.

E) Determine and formally prove the algorithm’s worst case space complexity.     
The worst case space complexity is $O(1)$ as it does not create a new list to store elements.


\pagebreak


## Recursive Insertion Sort
B) What is the worst case time complexity of this algorithm? Explain your answer.    
The worst case time copmplexity is still $O(n^2)$. Let's say the time complexity for recursively sorting the first n-1 element is $T(n-1)$, the running time for insert the last element in the sorted list is n. $T(n) = T(n-1) + n = T(n-2) + (n-1) + n = T(1) + T(2) + \dots + (n-1) + n = \frac{1}{2}n(n-1)$. Thus the time complexity for the worst case is still $O(n)$.

C) What is the worst case space complexity of your algorithm? Explain your answer.     
The space complexity is $O(1)$ as we did not create a new list to store elements. 



\pagebreak


## Sorting nearly sorted lists##      
For most part of the list, the innor loop will not execute as the order of the elements are already sorted. When there are unsorted parts, the inner loop will iterate a few times as the list is nearly sorted. Thus, it is faster than other sorting algorithms. 


\pagebreak


## Do you even Parentheses, Bro?##     
Time complexity: $O(n)$ as we have a for loop to loop through the full list.     
Space complexity: $O(n)$ since we create a new list and append elements into it. 


\pagebreak


## From Stacks to Queues##
For enqueue():    
Time complexity: $O(1)$     
Space complexity: $O(1)$     
For dequeue():     
Time complexity: $O(1)$ when there are elements in stack2 before we call dequeue(), $O(n)$ when stack2 is empty when we call dequeue()   
Space complexity: $O(n)$


\pagebreak


## Balanced Trees


\pagebreak


## Is Binary Tree Symmetric ##    
Time complexity: $O(n)$     
Space complexity: $O(h) = O(\log_2 n)$


\pagebreak


## Sum Root-To-Leaf Paths In A Binary Tree ##      
Time complexity: $O(n)$      
Space complexity: $O(h) = O(\log_2 n)$




\pagebreak
