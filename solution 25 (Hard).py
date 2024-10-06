class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def create_ListNodes(*values: int):
        if not values: return None

        head = ListNode(values[0])
        node = head

        for i in range(1, len(values)):
            node.next = ListNode(values[i])
            node = node.next
        
        return head
    
    @staticmethod
    def get_values_from_ListNodes(head) -> list[int]:
        values = []
        node = head

        while node:
            values.append(node.val)
            node = node.next
        
        return values

class Solution25:
    def reverseKGroupSlow(self, head: ListNode | None, k: int) -> ListNode | None:
        '''Slow version of reverseKGroup'''

        if not head: return None

        values, new_values = [], []
        node = head

        while node:
            values.append(node.val)
            node = node.next
        
        for i in range(0, len(values), k):
            new_values.extend(values[i + k - 1 : i - 1 : -1])

        merge = ListNode(new_values[0])
        node = merge

        for i in range(1, len(new_values)):
            node.next = ListNode(new_values[i])
            node = node.next
        
        return merge

    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        '''
        Повертає ListNode `head`, в якій кожна повна група із `k` елементів перевернута.

        ```
        reverseKGroup([1,2,3,4,5,6], 3) -> [3,2,1,6,5,4]
        reverseKGroup([1,2,3,4,5], 3) -> [3,2,1,4,5]
        ```
        '''
        
        if not head: return None

        # collection values
        values = []
        node = head

        while node:
            values.append(node.val)
            node = node.next
        
        # create new ListNode
        over_head = ListNode()
        node = over_head
        group_i = k - 1

        while group_i < len(values):
            for i in range(group_i, group_i - k, -1):
                node.next = ListNode(values[i])
                node = node.next
            
            group_i += k
        
        for i in range(group_i - k + 1, len(values)):
            node.next = ListNode(values[i])
            node = node.next
        
        return over_head.next

s = Solution25()
head = s.reverseKGroup(ListNode.create_ListNodes(1,2,3,4,5), 3)
print(ListNode.get_values_from_ListNodes(head))