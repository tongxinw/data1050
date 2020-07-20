# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] {"colab_type": "text", "id": "Z23HcXnk17kG"}
# # Dynamic Array
# ## Welcome to your first project in DATA1050!
#
# ## Before you start
# Before you start, enable extension manager and pair the notebook with a percent script through jupytext. 
#
# 1. [Enable extension manager](https://i.ibb.co/tP4vWk3/mng.png)
# 2. [Enable jupytext pairing](https://i.ibb.co/5LrtYcq/jupytext-enable.png)
#
# Jupytext converts python notebooks into python programs. Here we create `DynamicArray.py` in order to expose a pure script file for the testing framework.  You do not need to change `DynamicArray.py` file.
#

# %%
# Execute this cell to enable testing and automatic style check. 
# %pip install -q pytest
# %pip install -q pytest-cov

# %% [markdown]
# # Task 1.1: Warm-up

# %% [markdown] {"colab": {"base_uri": "https://localhost:8080/", "height": 51}, "colab_type": "code", "id": "aDQtD4iAUU5M", "outputId": "8a9d865b-a45f-4c64-efdf-1e2fe1287b84"}
# Here is a Dynamic Array Growth example to help your understanding.   
# Given a dynamic array with length 4, and capacity 5.   
# `[1,2,3,4, None]`
#
# Appending an additional is posible in O(1) time because the current array is not yet full.  
# `[1,2,3,4,5]`  
#
# When the array is full appending an element will cause the array to grow a factor K times it's current capacity.  
# `[1,2,3,4,5,6, None, None, None, None]`    
# The new array capacity is k times the old array capacity.  
#
# In order to grow the array, a new array must be allocated, and the contents of the old array must be copied over.   
# Below is some python code to simulate this operation.    
#

# %%
K = 2

old = [1, 2, 3, 4, 5]
old_capacity = 5

print(f'old = {old}')

new_element = 6
new = [None] * old_capacity * K
for i in range(old_capacity):
    new[i] = old[i]
new[old_capacity] = new_element
new_capacity = K * old_capacity

print(f'new = {new}')


# %% [markdown] {"colab_type": "text", "id": "y8b-Hdh0ywZP"}
# ## Support Code
# You do __not__ need to modify anything in this section, but you should run the section. It also might be helpful to read through the comments and code to understand what this class does. Use `FixedSizeArray` to implement `DynamicArray`. 
#

# %% {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "fY0zZBXSuQSZ", "outputId": "560fdb93-8cbf-4a03-87d2-a3b7e24bead6"}
class FixedSizeArray:
    """
    Fixed-size array class. 
    
    Use this as the data storage container when you implement DynamicArray. 
    DO NOT MODIFY.
    """
    # _access_count is a class variable that tracks how many times
    # `get`/`set` been called
    _access_count = 0

    def __init__(self, n):
        """
        Initializes `FixedSizeArray` of size `n` with all elements set to `None`.
        """
        if n <= 0:
            raise ValueError(
                "Tried to initialize `FixedSizeArray` with non-positive length")
        self._length = n
        self._internal_storage = [None] * n

    def __len__(self):
        return self._length

    def set(self, p, x):
        """
        Sets the element at position `p` to `x`. `p` should be in range [0,len(self)).
        """
        if p < 0 or p >= self._length:
            raise IndexError(
                "array index out of range, length is {} but tried to access "
                "index {}".format(self._length, p))
        FixedSizeArray._access_count += 1
        self._internal_storage[p] = x

    def get(self, p):
        """
        Returns the element at position `p`. `p` should be in range [0,len(self)).
        """
        if p < 0 or p >= self._length:
            raise IndexError(
                f"array index out of range, length is {self._length} but tried to "
                "access index {p}")
        FixedSizeArray._access_count += 1
        return self._internal_storage[p]

    def __str__(self):
        """
        Returns a printable string of the array content
        """
        return 'FixedSizeArray: ' + str(self._internal_storage)

    @classmethod
    def get_access_count(cls):
        """
        Returns the total number of times set() and get() have been called.
        """
        return cls._access_count


# %% [markdown]
# **Examples**

# %%
arr = FixedSizeArray(4)
print('Length:', len(arr))
arr.set(0, 3)
arr.set(2, 4)
print('The first element is:', arr.get(0))
print(arr)
print(arr.get_access_count())
#arr.set(5, 7) # Uncomment this line to see an error

# %% [markdown] {"colab_type": "text", "id": "iHVNDyakyJng"}
# # Task1.2: Let's start coding!
# Use the stencil code below to implement a `DynamicArray`.  Specifically, you will need to implement the methods `append`, `insert`, `pop` and `reverse`. 
# Your implementation should use a `FixedSizeArray` to store data internally, your methods will need to update and resize it as needed.
#
# __Tips:__
# - Remember to adjust the array length and capacity as needed. 
# - Create helper methods when necessary (there is at least one obvious one if you utilize the [DRY Principle](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself))!

# %% {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "8OvtptiGuUOz", "outputId": "9f19b163-709e-44ee-8da6-e8bb5ad46bdc"}
class DynamicArray:
    """
    This DynamicArray class provides set, get, append, insert, pop methods.  Data is stored internally 
    using a `FixedSizeArray` which is resized as needed. 

    TODO: Implement the requested methods and design tests for each.  Use the `FixedSizeArray` class 
    to allocate the necessary memory.
    
    HINT: Do not inherit 'FixedSizeArray'. 
    """

    MIN_CAPACITY = 4

    def __init__(self):
        """
        Returns an empty DynamicArray.
        """
        self._fixed_array = FixedSizeArray(self.MIN_CAPACITY)
        self._length = 0
        
    def __len__(self):
        return self._length
    
    def capacity(self):
        return len(self._fixed_array)
    
    def get(self, p):
        if p < 0 or p >= self._length:
            raise IndexError(
                'array index out of range, size is {} but tried to access '
                'index {}'.format(self._length, p))
        return self._fixed_array.get(p)

    def set(self, p, x):
        if p < 0 or p >= self._length:
            raise IndexError(
                'array index out of range, size is {} but tried to access '
                'index {}'.format(self._length, p))
        self._fixed_array.set(p, x)
        
    def adjust(self,grow):
        curr_cap = len(self._fixed_array)
        
        if grow:
            new = FixedSizeArray(curr_cap*2)
        else:
            new = FixedSizeArray(curr_cap//2)
            curr_cap = curr_cap//2
        
        for i in range(curr_cap):
            new.set(i,self._fixed_array.get(i))
        self._fixed_array = new

    def append(self, x):
        """ Add an item to the end of the current array. """
        # TODO: Implement me! Remember to update length and capacity as needed.
        
        if len(self) == len(self._fixed_array):
            grow = True
            self.adjust(grow)
        self._length += 1
        self.set(len(self)-1, x)
        # DONE
    
    def insert(self, i, x):
        """
        Insert an item `x` before position `i` of self.   
        Requires 0 <= i <= len(self), otherwise, `IndexError` is raised.
        """
        # TODO: Implement me! Remember to update length and capacity as needed.
        
        if i < 0 or i > len(self):
            raise IndexError(
                'array index out of range, size is {} but tried to access '
                'index {}'.format(self._length, i))
        else:
            if len(self) == self.capacity():
                grow = True
                self.adjust(grow)
            
            self._length += 1
            for j in range(len(self)-1,i,-1):
                self.set(j,self.get(j-1))
            self.set(i, x)

    def pop(self, i=None):
        """
        Remove the item at position `i` of self, and return
        it. a.pop() removes and returns the last item in self. 
        Requires 0 <= i < len(self), otherwise, `IndexError` is raised.
        """
        # TODO: Implement me! Remember to update length and capacity as needed.
        if i == None:
            i = len(self)-1
            
        if i < 0 or i >= len(self):
            raise IndexError(
                'array index out of range, size is {} but tried to access '
                'index {}'.format(self._length, i))   
        else:
            elem = self.get(i)
            for ind in range(i,len(self)-1):
                self.set(ind,self.get(ind+1))
            self.set(len(self)-1,None)
            self._length -= 1
        if self._length <= self.capacity()//4:
            grow = False
            self.adjust(grow)
        return elem
        
    def reverse(self):
        """
        Reverse the elements of the self, in place.
        """
        # TODO: Implement me!
        for i in range(len(self)//2):
            temp = self._fixed_array.get(i)
            self._fixed_array.set(i, self._fixed_array.get(len(self)-1-i))
            self._fixed_array.set(len(self)-1-i,temp)

    def __str__(self):
        return f'DynamicArray: capacity={len(self._fixed_array)}, length={self._length}; Internal {self._fixed_array}; '


    

# %% [markdown]
# **Examples**

# %%
arr = DynamicArray()
print('Length:', len(arr))
arr.append(3)
print(arr)
arr.append(4)
print('The first element is:', arr.get(0))
print(arr)

arr.insert(2,5)
print(arr)

arr.insert(0,'test')
print(arr)

arr.reverse()
print(arr)

print(arr.pop(0))
print(arr)

# #arr.set(5, 7) # Uncomment this line to see an error



# %% [markdown] {"colab_type": "text", "id": "KAV_8TWlyoW6"}
# # Task1.3 Let's write some tests
# Testing is a critical part of programming! Refer to the handout for more information about things you should keep in mind when writing tests.

# %% {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "GUnFT1BPuUYL", "outputId": "4c158239-3090-4228-db4e-e0ebca9c8b05"}
import pytest


def assert_dynamic_array_equal(a, b):
    assert len(a) == len(b)
    for i in range(len(b)):
        assert a.get(i) == b[i]


def test_init():
    dl = DynamicArray()
    assert_dynamic_array_equal(dl, [])
    # Example of Exception testing
    with pytest.raises(IndexError):
        dl.pop()
    with pytest.raises(IndexError):
        dl.get(0)


def test_append():
    dl = DynamicArray()
    dl.append(1)
    dl.append(2)
    assert_dynamic_array_equal(dl, [1, 2])
    dl.append('test')
    assert_dynamic_array_equal(dl, [1, 2, 'test'])
    

# TODO: add test cases for your methods

def test_insert():
    dl = DynamicArray()
    dl.append(1)
    dl.append(2)
    assert_dynamic_array_equal(dl, [1, 2])
    dl.insert(0,'test')
    assert_dynamic_array_equal(dl, ['test',1,2])
    

def test_pop():
    dl = DynamicArray()
    dl.append(1)
    dl.append(4)
    dl.append('test')
    dl.append(5)
    assert_dynamic_array_equal(dl, [1, 4,'test',5])
    dl.append(7)
    assert_dynamic_array_equal(dl, [1, 4,'test', 5, 7])
    dl.pop(1)
    dl.pop(1)
    dl.pop(1)
    dl.pop(1)
    assert_dynamic_array_equal(dl, [1])
    
def test_reverse(): 
    dl = DynamicArray()
    dl.append(1)
    dl.append(4)
    dl.append('test')
    dl.append(5)
    assert_dynamic_array_equal(dl, [1, 4,'test',5])
    dl.reverse()
    print(dl)
    assert_dynamic_array_equal(dl, [5,'test', 4, 1])



# %% {"colab": {}, "colab_type": "code", "id": "m2-bpX41PrtG"}
# Execute this cell to start the test. SAVE the notebook to flushes changes to storage.
# Note that pytest only works on `DynamicArray.py` files. So jupytext pairing mentioned at the very beginning is necessary.
# !python3 -m pytest --cov-report term --cov-report=annotate DynamicArray.py --cov

# %% {"language": "bash"}
# # Use this cell to show the lines not yet covered in your test
# # Lines begining with '!' is not covered by your tests
# grep --color=always -C 4 -E "^!.*\$" "DynamicArray.py,cover"

# %%
