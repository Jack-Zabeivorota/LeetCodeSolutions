from typing import Literal


class Node:
    def __init__(self, value: int, next: 'Node' = None, prev: 'Node' = None):
        self.value = value
        self.next = next
        self.prev = prev


class MyCircularDeque:
    '''Simple deque'''

    def __init__(self, max_len: int):
        self.len = 0
        self.max_len = max_len
        self.first = self.last = None
        

    def _addItem(self, value: int, mode: Literal['first', 'last']) -> bool:
        if self.len == 0:
            self.first = self.last = Node(value)
            self.len = 1
            return True
        
        if self.len == self.max_len:
            return False
        
        if mode == 'first':
            self.first = Node(value, self.first)
            self.first.next.prev = self.first
        else:
            self.last = Node(value, None, self.last)
            self.last.prev.next = self.last

        self.len += 1
        return True


    def insertFront(self, value: int) -> bool:
        return self._addItem(value, 'first')
        

    def insertLast(self, value: int) -> bool:
        return self._addItem(value, 'last')
        

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        
        if self.len == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.prev = None
        
        self.len -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        
        if self.len == 1:
            self.first = self.last = None
        else:
            self.last = self.last.prev
            self.last.next = None
        
        self.len -= 1
        return True


    def getFront(self) -> int:
        return self.first.value if not self.first else -1
        

    def getRear(self) -> int:
        return self.last.value if not self.last else -1


    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.max_len


obj = MyCircularDeque(2)
print(obj.isEmpty())
print(obj.insertFront(5))
print(obj.insertLast(8))
print(obj.isFull())
print(obj.getFront())
print(obj.getRear())
print(obj.deleteFront())
print(obj.deleteLast())