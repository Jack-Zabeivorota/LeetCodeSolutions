from typing import Callable, Any


class TreeNode:
    def __init__(self, x: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = x
        self.left = left
        self.right = right

class Solution297:
    '''Серіалізація та десеріалізація бінарного дерева'''

    # without recursion

    def _recursion(self, func: Callable[[dict, Any], dict | None], state: dict, collector=None):
        stack = [state]

        while stack:
            state = func(stack[-1], collector)
            stack.pop() if state is None else stack.append(state)

    def _serialize_iteration(self, state: dict, collector: list[str]) -> dict | None:
        stage: int     = state['stage']
        node: TreeNode = state['node']

        if stage == 1:
            if node:
                collector.append(str(node.val))
                state['stage'] = 2
                return { 'node': node.left, 'stage': 1 }
            
            collector.append('n')
            return

        if stage == 2:
            state['stage'] = 3
            return { 'node': node.right, 'stage': 1 }

    def serialize1(self, root: TreeNode) -> str:
        collector = []

        self._recursion(
            self._serialize_iteration,
            { 'node': root, 'stage': 1 },
            collector
        )

        return ';'.join(collector)

    def _data_to_values(self, data: str) -> list[int | None]:
        values = data.split(';')

        for i in range(len(values)):
            if values[i] == 'n':
                values[i] = None
            else:
                values[i] = int(values[i])
        
        return values

    def _deserialize_iteration(self, state: dict, collector: dict) -> dict | None:
        stage: int               = state['stage']
        values: list[int | None] = collector['values']
        index: int               = collector['index']

        if stage == 1:
            if values[index] is None:
                collector['answer'] = None
                return
    
            state['node'] = TreeNode(values[index])
            state['stage'] = 2

            collector['index'] += 1
            return { 'stage': 1 }
        
        if stage == 2:
            state['node'].left = collector['answer']
            state['stage'] = 3

            collector['index'] += 1
            return { 'stage': 1 }

        state['node'].right = collector['answer']
        collector['answer'] = state['node']

    def deserialize1(self, data: str) -> TreeNode:
        if data in ['', 'null']:
            return None

        collector = { 'values': self._data_to_values(data), 'index': 0, 'answer': None }

        self._recursion(
            self._deserialize_iteration,
            { 'stage': 1 },
            collector
        )

        return collector['answer']


    # with recursion

    def serialize(self, root: TreeNode) -> str:
        collector = []

        def serialize_node(node: TreeNode | None):
            if node:
                collector.append(str(node.val))
                serialize_node(node.left)
                serialize_node(node.right)
            else:
                collector.append('n')

        serialize_node(root)
        return ';'.join(collector)

    def deserialize(self, data: str) -> TreeNode:
        if data in ['', 'null']:
            return None
        
        values = data.split(';')
        self.i = 0

        def deserialize_node() -> TreeNode:
            if values[self.i] == 'n':
                return None

            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = deserialize_node()
            self.i += 1
            node.right = deserialize_node()
            
            return node

        return deserialize_node()

def tn(x, left, right):
    return TreeNode(x, left, right)

root = tn(4,
          tn(-7, None, None),
          tn(-3,
             tn(-9,
                tn(9,
                   tn(6,
                      tn(0, None, tn(-1, None, None)),
                      tn(6, tn(-4, None, None), None)),
                   None),
                tn(-7,
                   tn(-6, tn(6, None, None), None),
                   tn(-6,
                      tn(9, None, tn(-2, None, None)),
                      None))),
             tn(-3, tn(-4, None, None), None)))

s = Solution297()
print(s.serialize(s.deserialize(s.serialize(root))))