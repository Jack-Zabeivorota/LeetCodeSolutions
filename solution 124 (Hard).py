from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class NodeData:
    def __init__(self, node: TreeNode):
        self.node = node
        self.left_val = None if node.left else 0
        self.right_val = None if node.right else 0
    
    def get_total(self) -> int:
        return self.left_val + self.node.val + self.right_val

    def get_max_val(self) -> int:
        max_val = max(self.left_val, self.right_val) + self.node.val
        return max_val if max_val >= 0 else 0

class Solution124:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Повретає найбільший шлях (суму узлів) із дерева `root`, не використовующи рекурсію.

        ```
        #  -10
        #  /  \\
        # 9    20
        #     /  \\
        #    15   7
        
        result: 15 + 20 + 7 = 42
        ```
        '''

        if not root: return 0

        max_total = root.val
        nodes_data = [NodeData(root)]

        while True:
            node_data = nodes_data[-1]

            if node_data.left_val is None:
                nodes_data.append(NodeData(node_data.node.left))

            elif node_data.right_val is None:
                nodes_data.append(NodeData(node_data.node.right))
                
            else:
                max_total = max(max_total, node_data.get_total())
                nodes_data.pop()
                
                if not nodes_data: break

                prev_node_data = nodes_data[-1]

                if prev_node_data.left_val is None:
                    prev_node_data.left_val = node_data.get_max_val()
                else:
                    prev_node_data.right_val = node_data.get_max_val()
        
        return max_total

s = Solution124()
print(s.maxPathSum(TreeNode(
    1,
    TreeNode(-2),
    TreeNode(3, TreeNode(1))
)))