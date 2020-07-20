import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0, os.path.join(parentdir, 'stencil'))
from test_framework import generic_test


class Queue:
    """
    implement a queue using methods from stack.
    """
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, x): 
        """
        Add input x to queue; no output.
        """
        
        self.stack1.append(x)
        return
    def dequeue(self):
        """
        remove an element from the end of the queue.
        """
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            if self.stack2:
                return self.stack2.pop()
        else:
            return self.stack2.pop()


def test_Queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    print("All tests pass!")
test_Queue()


def queue_tester(ops):
    from test_framework.test_failure import TestFailure

    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_from_stacks.py",
                                       'queue_from_stacks.tsv', queue_tester))
