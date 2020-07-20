# +
#     def heapify(arr, i): 
#         n = len(arr)
#         smallest = i # Initialize smalles as root  
#         l = 2 * i + 1 # left = 2*i + 1  
#         r = 2 * i + 2 # right = 2*i + 2  

#         # If left child is smaller than root  
#         if l < n and arr[l] < arr[smallest]:  
#             smallest = l  

#         # If right child is smaller than  
#         # smallest so far  
#         if r < n and arr[r] < arr[smallest]:  
#             smallest = r  

#         # If smallest is not root  
#         if smallest != i:  
#             (arr[i],  
#              arr[smallest]) = (arr[smallest], arr[i]) 
#             # Recursively heapify the affected 
#             # sub-tree  
#             heapify(arr)


def argmin(L, ind):
    ind = ind if ind is not None else range(len(L))
    return min(ind, key=L.__getitem__)

def argmax(L, ind):
    ind = ind if ind is not None else range(len(L))
    return max(ind, key=L.__getitem__)

class myBinHeap:
    
    def __init__(self, key=None):
        self.heapList = []
        self.currentSize = 0
        if key is None:  # no key in use
            self.key = lambda x: x  # needed for insert/percUp
            self.percDown = self.percDown_no_key
        else:  # key in use
            self.key = key
            self.percDown = self.percDown_key
            
    def percUp(self,i):
        while (i + 1) // 2 >= 1: 
            if self.key(self.heapList[i]) < self.key(self.heapList[(i - 1) // 2]): 
                tmpr = self.heapList[(i - 1) // 2]
                self.heapList[(i - 1) // 2] = self.heapList[i]
                self.heapList[i] = tmpr
            i = (i - 1) // 2

    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize - 1)
            
    def minChild(self,i):
        if i * 2 + 3 > self.currentSize:
            return i * 2 + 1
        else:
            if self.heapList[i * 2 + 1 ] < self.heapList[i * 2 + 2]:
                return i * 2 + 1
            else:
                return i * 2 + 2
            
    def percDown_no_key(self,i):
        while self.currentSize >= (i * 2 + 2) :
            if i * 2 + 3 > self.currentSize:
                mc = i * 2 + 1
            else:
                if self.heapList[i * 2 + 1] < self.heapList[i * 2 + 2]:
                    mc = i * 2 + 1
                else:
                    mc = i * 2 + 2
            if self.heapList[i] > self.heapList[mc]:
                tmpr = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmpr
            i = mc
            
            
    def percDown_key(self,i):
        while self.currentSize >= (i * 2 + 2):
            if i * 2 + 3 > self.currentSize:
                mc = i * 2 + 1
            else:
                if self.key(self.heapList[i * 2 + 1]) < self.key(self.heapList[i * 2 + 2]):
                    mc = i * 2 + 1
                else:
                    mc = i * 2 + 2
            if self.key(self.heapList[i]) > self.key(self.heapList[mc]):
                tmpr = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmpr
            i = mc
            
    def percDown_minChild_no_key(self,i):
        while self.currentSize >= (i * 2 + 2):
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]: 
                tmpr = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmpr
            i = mc
            
    def percDown_argmin_no_key(self, i):
        while self.currentSize >= (i * 2 + 2): 
            mc = 2 * i + 1
            if 2 * i + 3 <= self.currentSize:
                mc = argmin(self.heapList, [2 * i + 1, 2 * i + 2])
            if self.heapList[i] > self.heapList[mc]:
                tmpr = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmpr
            i = mc
            
    def delMin(self):
        retval = self.heapList[0]
        self.heapList[0] = self.heapList[self.currentSize - 1]
        self.heapList[self.currentSize - 1] = retval
        self.currentSize -= 1
        self.percDown(0)
        return retval

        
    def buildHeap(self,alist):
        i = len(alist)// 2 - 1
        self.currentSize = len(alist)
        self.heapList = alist # need to change it to inplace
        while (i >= 0):
            self.percDown(i)
            i -= 1


# -

def test_myBinHeap():
    l = [5,2,4]
    mbh = myBinHeap()
    mbh.buildHeap(l)
    mbh.insert(1)
    assert mbh.delMin() == 1
    assert mbh.delMin() == 2
    assert mbh.delMin() == 4
    assert mbh.delMin() == 5
    
    l = myBinHeap(key = lambda x:x)
    L = [1,5,10,9,6,7]
    l.buildHeap(L)
    assert l.delMin() == 1
    
    
    percDown_no_key = myBinHeap.percDown_no_key
    myBinHeap.percDown_no_key = myBinHeap.percDown_argmin_no_key
    bh = myBinHeap()
    bh.buildHeap([1,3,2,6,9])
    assert bh.delMin() == 1
    assert bh.delMin() == 2
    assert bh.delMin() == 3
    assert bh.delMin() == 6
    assert bh.delMin() == 9
    myBinHeap.percDown_no_key = percDown_no_key
    
    
    percDown_no_key = myBinHeap.percDown_no_key
    myBinHeap.percDown_no_key = myBinHeap.percDown_minChild_no_key
    bh = myBinHeap()
    bh.buildHeap([1,3,2,6,9])
    assert bh.delMin() == 1
    assert bh.delMin() == 2
    assert bh.delMin() == 3
    assert bh.delMin() == 6
    assert bh.delMin() == 9
    myBinHeap.percDown_no_key = percDown_no_key
    
    assert argmin([1,2],[0,1]) != 1
    assert argmax([1,2],[0,1]) != 0
    
    print("Yeah!!! pass all test~")

test_myBinHeap()




