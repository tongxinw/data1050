# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] {"colab_type": "text", "id": "Z23HcXnk17kG"}
# # LRU Cache 
# This project should help familiarize you with two kinds of data structures: doubly linked lists and dictionaries. In this project, you'll implement a Least Recently Used (LRU) Cache comprised of these two data structures. 
#
# ## Before you start
# Before you start, enable extension manager and pair the notebook with a percent script through jupytext. 
#
# 1. [Enable extension manager](https://i.ibb.co/tP4vWk3/mng.png)
# 2. [Enable jupytext pairing](https://i.ibb.co/5LrtYcq/jupytext-enable.png)
#
#

# %%
# Execute this cell to enable testing and automatic style check. 
# Please resolve all style warnings reported by `%%flake8` before submission.

# %pip install -q pytest pytest-cov 

# %% [markdown]
# # Task 2.1 DoublyLinkedList

# %% {"colab": {"base_uri": "https://localhost:8080/", "height": 51}, "colab_type": "code", "id": "aDQtD4iAUU5M", "outputId": "8a9d865b-a45f-4c64-efdf-1e2fe1287b84"}
class ListNode:
    '''Doubly linked list node.'''
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.data = val
        
    def __str__(self):
        """ Return string representation of data in this node and all successor nodes """
        node = self
        visited = set()
        first = True
        result = ''

        while node:
            if first:
                first = False
            else:
                result += ' -> '
            if id(node) in visited:
                if node.next is not node:
                    result += str(node.data)
                    result += ' -> ... -> '
                result += str(node.data)
                result += ' -> ...'
                break
            else:
                result += str(node.data)
                visited.add(id(node))
            node = node.next
        return result


class DoublyLinkedList:
    """
    A linked list container built on `ListNode`. Two pseudo nodes are used for
    head and tail.
    """

    def __init__(self):
        self.head = ListNode(None)  # pseudo-node
        self.tail = ListNode(None)  # pseudo-node
        self.head.next = self.tail
        self.tail.prev = self.head
        self._length = 0

    def __len__(self):
        return self._length

    def get_last(self):
        """ Returns the last node (psedu-node is skipped). 
        Raises IndexError when no node exists. """
        if self._length == 0:
            raise IndexError("Try to get item from an empty LinkedList")
        return self.tail.prev

    def prepend(self, node):
        """
        Insert `node` at the head of the linked list
        """  
        # TODO: implement me
        
        new_node = node
        
        if self._length == 0:
            new_node.next = self.tail
            new_node.prev = self.head
            self.head.next = new_node
            self.tail.prev = new_node
            
        else:
            old_head = self.head.next
            new_node.next = old_head
            old_head.prev = new_node
            self.head.next = new_node
            new_node.prev = self.head
            
        self._length += 1
        
        return self    

    def remove(self, node):
        """
        Remove `node` from this linked list
        """  
        # TODO: implement me

        # empty list
        if self._length == 0:
            raise IndexError("Try to remove item from an empty LinkedList")
        # TODO: node not in list
        else:
            key = self.head.next
            while key.data != node.data:
                key = key.next
#                 if key == None:
#                     raise IndexError("Node not in LinkedList")
            key.prev.next = key.next
            key.next.prev = key.prev
        
        self._length -= 1
        return self    
            


    def __str__(self):
        return str(self.head)
        
    class HasLoopException(Exception):
        pass

# %%
# Examples for DoublyLinkedList
l = DoublyLinkedList()
n2 = ListNode(2)
n1 = ListNode(1)
n3 = ListNode(3)

l.prepend(n2)
l.prepend(n1)
print(l)

#l.remove(n2)
l.remove(n1)
print(l)


# %% [markdown] {"colab_type": "text", "id": "y8b-Hdh0ywZP"}
# # Task2.2 LRU Cache

# %% {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "fY0zZBXSuQSZ", "outputId": "560fdb93-8cbf-4a03-87d2-a3b7e24bead6"}
class LRUCache:
    """
    A "Least Recent Used" cache. This cache holds 
    up to `capacity` key-value pairs. Adding a new key when the cache is full (via put)
    results in the least recently key-value pair is removed.
    """

    def __init__(self, capacity=4):
        '''Create a LRUCache with of size capacity.'''
        if capacity < 1:
            raise ValueError(
                "capacity should be >=1 but {} given".format(capacity))
        self.capacity = capacity

        # This linked list records the key-value pair in the order of their recentness.
        self.list = DoublyLinkedList()

        # dictionay that maps keys to linked list node for quicker node lookup
        self.map = {}

    def __len__(self):
        return len(self.list)

    def __contains__(self, key):
        """ Magic method for checking key existence

        Examples: 
            if 'key' in lru_dict:
                print("exist!")
        """
        return key in self.map

    def put(self, key, value):
        """
        Adds (key, value) to cache. If the cache is full, and the key is new,
        the least recently (key,value) pair is removed.
        """
        # TODO: implement the following:
        # If the key already exists in the self.map dict,
        # replace the key-value pair stored in the linked list. 
        if key in self:
            n = self.map[key]
            n.data = (key,value)
            # self.map[key] = ListNode(value)
            self.list.remove(n)
            self.list.prepend(n)
            
        # If the key does not exist, add this key-value pair to self.list.  If
        # self.map is over capacity, evict the least recent used key-value.
        # Also be sure to update the LRU order in self.list.
        else:
            if len(self.list) == self.capacity:
                last_n = self.list.get_last()
                self.list.remove(last_n)
                del self.map[last_n.data[0]]
            self.map[key] = ListNode((key,value))
            self.list.prepend(self.map[key])

    def get(self, key, default=None):
        """
        Get value for `key`. Return `default` when the key is not found.
        """
        # TODO: implement me
        # If the key exists in self.map, return the value and update the LRU order in self.list.
        if key in self:
            n = self.map[key]
            self.list.remove(n)
            self.list.prepend(n)
            return self.map[key].data[1]
        # If the key does not exist return the default value.
        else:
            return default


    def items(self):
        """
        return all key-value pairs in the order of recentness (the most recent to the least recent)
        """
        # TODO: implement me
        pair_list = []
        n = self.list.head.next
        while n != self.list.tail:
            pair_list.append(n.data)
            n = n.next
        return pair_list
    
    def __str__(self):
        """
        return str representation of self.items()
        """
        return "LRUCache:\n" + '\n'.join([f"key={k}, value={v}" for k, v in self.items()])

# %%
# Examples for LRUCache
d = LRUCache(2)
d.put('k', 1)
d.put('v', 2)
d.put('a',1)
print(d.list.get_last().data)

# %%
d.get('a')

# %%
print(d)

# %% [markdown] {"colab_type": "text", "id": "iHVNDyakyJng"}
# # Task2.3 Testing

# %% {"colab": {"base_uri": "https://localhost:8080/", "height": 34}, "colab_type": "code", "id": "8OvtptiGuUOz", "outputId": "9f19b163-709e-44ee-8da6-e8bb5ad46bdc"}
import pytest
import random
from typing import Any


class DefaultValue:
    def __eq__(self, other):
        return isinstance(other, DefaultValue)


def assert_miss(d, key):
    assert key not in d.map
    assert isinstance(d.get(key, DefaultValue()), DefaultValue)


def test_example():
    ld = LRUCache(2)
    assert_miss(ld, 'a')        # should miss
    ld.get(3, None)
    

def test_list_repr_with_cycle():
    # help boosting coverage by testing LinkedList.__str__
    l = DoublyLinkedList()
    last = ListNode(3)
    l.prepend(last)
    l.prepend(ListNode(2))
    first = ListNode(1)
    l.prepend(first)
    last.next = first
    assert str(l) == "None -> 1 -> 2 -> 3 -> 1 -> ... -> 1 -> ..."

# TODO: add more tests
def test_put():
    d = LRUCache(2)
    d.put('k', 1)
    d.put('v', 2)
    d.put('a',1)

    assert d.list.get_last().data == ('v',2)
    
    
def test_get():
    d = LRUCache(2)
    d.put('k', 1)
    d.put('v', 2)

    d.put('a',1)
    d.put('k',3)
    assert d.get('k') == 3



# %% {"colab": {}, "colab_type": "code", "id": "m2-bpX41PrtG"}
# execute this cell to start the test.
# !pytest --cov-report term --cov-report=annotate LRUCache.py --cov .

# %% {"language": "bash"}
# # Lines begining with '!' is not covered by your tests
# grep --color=always -C 4 -E "^!.*$" "LRUCache.py,cover"

# %% [markdown]
# # Task2.4 Application: Memorization

# %%
from functools import lru_cache
_call_count = 0

@lru_cache(maxsize=10)
def fibonacci(n):
    global _call_count
    _call_count += 1
    if n <= 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)
    # return fibonacci(n - 1) + fibonacci(n - 2)
    
r = fibonacci(20)
assert r == 6765
print('result:', r)
print('# of function calls:', _call_count)
print(fibonacci.cache_info())
