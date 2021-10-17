from dataclasses import dataclass
from typing import Any, Sized

# A head-and-tail implementation of a deque using data classes
# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as first entry in deque
    def add_first(self, n):
        node = Node()
        node.value = n
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.nxt = self.head
            self.head = node
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        if self.size == 0:
            print("Error empty deque")
            return None
        else:
            return f"Head? {self.head.value}, tail? {self.tail.value}, size? {self.size}"

    # Add element n as last entry in deque
    def add_last(self, n):
        node = Node()
        node.value = n
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node
        self.size += 1
        

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.tail == None:
            print("Error empty deque")
            return None
        return self.tail

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head == None:
            print("Error empty deque")
            return None
        return self.head

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 0:
            print("Error empty deque")
            return None
        elif self.size == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.nxt
        self.size -= 1
        return self.head
        

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        print(self.size)
        if self.size == 0:
            print("Error empty deque")
            return None
        elif self.size == 1:
            self.tail = None
            self.head = None
        else:
            nxt = self.head
            for i in range(self.size-2):
                print(i, self.size)
                print(nxt)
                nxt = nxt.nxt
            nxt.nxt = None
            self.tail = nxt
        self.size -= 1
        return self.tail
