from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ids = set()
        
        while head:
            if id(head) in ids:
                return True
            ids.add(id(head))
            head = head.next

        return False
        
    
    def printListNode(self, head: Optional[ListNode]):
        list_node = []

        if head:
            while head.next: 
                list_node.append(head.val)
                head = head.next
            list_node.append(head.val)

            return list_node
        else:
            return None
    
    def listify (self, lst: list) -> Optional[ListNode]:
        listified = ListNode()
        curr = listified

        if lst:
            for i in range(len(lst)-1):
                curr.val, curr.next = lst[i], ListNode()
                curr = curr.next

            curr.val = lst[-1]

            return listified    
        else:
            return None
        
def main():
    s = Solution()

    print('head = [3,2,0,-4], pos = 1:', s.hasCycle(head = s.listify([3,2,0,-4])))
    print('head = [1,2], pos = 0:', s.hasCycle(head = s.listify([1,2])))
    print('head = [1], pos = -1:', s.hasCycle(head = s.listify([1])))

if __name__ == '__main__':
    main()