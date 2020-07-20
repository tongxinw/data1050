#!/usr/bin/env python
# coding: utf-8
# %%
from myBinHeap import myBinHeap


# %%
def heap_sort(L, key = None):
    bh = myBinHeap(key = key)
    bh.buildHeap(L)
    for i in range(len(L)):
        bh.delMin()
    return L

# %%



# def heap_Sort(arr): 
#     n = len(arr)
#     # Build heap (rearrange array)  
#     for i in range(int(n / 2) - 1, -1, -1): 
#         heapify(arr, n, i)  
  
#     # One by one extract an element 
#     # from heap  
#     for i in range(n-1, -1, -1): 
          
#         # Move current root to end # 
#         arr[0], arr[i] = arr[i], arr[0] 
  
#         # call max heapify on the reduced heap  
#         heapify(arr, i, 0) 

# %%
def heap_sort_stable(L, key=None): 

    bh = myBinHeap(key=key)
    if key is None:
        key = lambda x:x
    
    end = []
    dic = {}
    for i in L:
        if key(i) not in dic:
            dic[key(i)] = [i]
        else:
            dic[key(i)].append(i)
    bh.buildHeap(L)
    for j in range(len(L)):
        end += [dic[key(bh.delMin())].pop()]
    L[:] = end
    return L

# %%
