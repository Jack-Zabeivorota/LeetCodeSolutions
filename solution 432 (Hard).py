class Node:
    def __init__(self, num: int, next: 'Node' = None, prev: 'Node' = None):
        self.num = num
        self.keys = set()
        self.next = next
        self.prev = prev


class AllOne:
    '''
    Структура даних, яка зберігає кількість рядків із можливістю
    повернення рядків із мінімальною та максимальною кількістю.
    
    Кожна операція (inc, dec, getMinKey, getMaxKey) виконується
    за константний час O(1).
    '''

    def __init__(self):
        self.nodes: dict[str, Node] = {}
        self.first: Node | None = None
        self.last: Node | None = None
    

    def _remove_node(self, node: Node):
        if node is self.first:
            self.first = node.next
        else:
            node.prev.next = node.next

        if node is self.last:
            self.last = node.prev
        else:
            node.next.prev = node.prev


    def inc(self, key: str):
        if not self.first:
            self.first = self.last = Node(1)
        
        if key in self.nodes:
            old_node = self.nodes[key]
            num = old_node.num + 1
            old_node.keys.remove(key)

            if old_node.next and old_node.next.num == num:
                node = old_node.next
            else:
                node = Node(num, old_node.next, old_node)
                old_node.next = node

                if node.next:
                    node.next.prev = node
                else:
                    self.last = node
                
            node.keys.add(key)
            self.nodes[key] = node

            if not old_node.keys:
                self._remove_node(old_node)
        else:
            if self.first.num != 1:
                self.first = Node(1, self.first)
                self.first.next.prev = self.first

            self.first.keys.add(key)
            self.nodes[key] = self.first
    

    def dec(self, key: str):
        if not key in self.nodes:
            return
        
        old_node = self.nodes[key]
        num = old_node.num - 1
        old_node.keys.remove(key)

        if num > 0:
            if old_node.prev and old_node.prev.num == num:
                node = old_node.prev
            else:
                node = Node(num, old_node, old_node.prev)
                old_node.prev = node

                if node.prev:
                    node.prev.next = node
                else:
                    self.first = node
                    
            node.keys.add(key)
            self.nodes[key] = node
        else:
            del self.nodes[key]

        if not old_node.keys:
            self._remove_node(old_node)
    

    def getMinKey(self) -> str:
        return next(iter(self.first.keys)) if self.first else ''


    def getMaxKey(self) -> str:
        return next(iter(self.last.keys)) if self.last else ''
    

    def printNodes(self):
        node = self.first

        while node:
            print(node.num, node.keys)
            node = node.next


obj = AllOne()
obj.inc('a')
obj.inc('b')
obj.dec('a')
obj.inc('a')
obj.inc('b')
obj.inc('c')
obj.printNodes()
print(obj.getMaxKey())
print(obj.getMinKey())