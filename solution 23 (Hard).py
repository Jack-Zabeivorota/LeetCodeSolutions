class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution23:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        '''
        Здійснює зливання всіх ланцюгів з узлів зі списку `lists` в однин ланцюг з узлів,
        значення яких розташовані по зростанню.

        ```
        mergeKLists([
            [5 -> 8 -> 2],
            [6 -> 2 -> 1],
            [3 -> 10]
        ])
        result: [1 -> 2 -> 2 -> 3 -> 5 -> 6 -> 8 -> 10]
        ```
        '''

        if not lists: return None
        
        values = []

        while lists:
            next_lists = []

            for node in lists:
                if node is None: continue
                values.append(node.val)
                
                if not node.next is None:
                    next_lists.append(node.next)
            
            lists = next_lists
        
        if not values: return None
        values.sort()

        node_merge = ListNode(values[0])
        node = node_merge

        for i in range(1, len(values)):
            node.next = ListNode(values[i])
            node = node.next
        
        return node_merge
                

s = Solution23()
print(s.mergeKLists([1,2,0]))