<!-- #region -->
# LRU Cache Report

Banner ID: 

-----

## Q2.1
Prepend - Using array requires time complexity of O(n), and using singly-linked list requires time complexity of O(n);

Remove - using array reqiresd time complexity of O(n), while using singly-linked list requires time complexity of is O(n) by finding the predecessor node and change the next pointer of it to the current next node.


## Q2.2
To remove a node in a singly linked list, we need to know its predecessor and the change its next pointer to the current next node since the current node does not store the data of the location of the predecessor next pointer (it is one-way), and the time complexity is O(n); while removing a node in doubly linked list, we need to change the next pointer of the predecessor to next of current node, we do not need to access the previous node, and the time complexity is O(1).  

To get the previous node, sometimes the list is traversed. In DLL, we can get the previous node using previous pointer.


## Q2.3

Scanning would have the most number of misses, and then is random, locality has the least number of misses. 

## Q2.4

Both of worst cases would be O(n) as the node we need might be around the tail of the linked list.  

## Q2.5

Although singly liked list uses less memory, while removing/prepending from the list, sometimes we need to travel the whole list to get the previous node, which might have a time complexity of O(n); however, for doubly linked list, we can get the previous node using the prev pointer, which has time complexity of O(1). When we have a long list, doubly linked list will be faster. 

## Q2.6

1. 13529
2. 20
3. The mininum cache size with could have the same benefit is 2. The LRU feature performs best when maxsize is a power-of-two, and the least positive integer power of 2 is 2. 
4. Even we rearrange the order of the recursive steps, we still get the same result. 
5. "misses" corresponds to _call_count, and it means the count of time when the data requested is not in the cache; 'hits' means the count of times when data is required exists in the cache; 'maxsize' means the maximum number of caches could be saved; 'currsize' means the number of caches being saved now. 
6. fibonacci.cache_clear(); we might need to clear the memorizatioin cache when the url data gets updated, then we can keep the cache updated. 
<!-- #endregion -->
