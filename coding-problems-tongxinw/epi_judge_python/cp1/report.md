<!-- #region -->
**buy_and_sell_stock_once(prices):**      
The method first gets the first entry in the array, so time complexity is O(1). There is only 1 for loop to check all the elements in the string once, so the time complexity is O(n);When n is relatively large, the time complexity is O(n). The space compplexity is O(1) since we did not create a new string to store values. 

**is_palindrome(s):**   
For this method, since we are using two indices (one from the beginning and one from the end), and the beginning index will alwasy be smaller than the end index, the time complexity will be O(n), and the sapce complexity is O(1) since we did not create a new array to store the string.     


**dutch_flag_partition(pivot_index, A):**     
The index starts from 0, and if the elements in the array is less than the pivot, we move them to the front of the array, so time complexity is O(n). When we move the larger elements to the end of the array, we only check until when the elements are not less than the pivot, so the time complexity is less than O(n), then the total time complexity is still O(n). The space complexity is O(1) since the function did not create a new array to store values. 
<!-- #endregion -->
