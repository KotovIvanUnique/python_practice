from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        counter = 0
        reversed = None
        
        if not head:
            return None
        
        curr = head
        
        while curr.next:            
            reversed = ListNode(curr.val, reversed)
            curr = curr.next
            counter += 1

        reversed = ListNode(curr.val, reversed)

        reversed_curr = reversed
        curr = head.next
        to_replace = counter//2

        while to_replace > 0:
            curr.val, curr.next = reversed_curr.val, ListNode(curr.val, curr.next)
            reversed_curr = reversed_curr.next
            to_replace -= 1

            if to_replace > 0:
                curr = curr.next.next
            else:
                if counter%2 > 0:
                    curr.next.next.next = None
                else:
                    curr.next.next = None
    
    def printListNode(self, head: Optional[ListNode]):
        list_node = []

        while head.next: 
            list_node.append(head.val)
            head = head.next
        list_node.append(head.val)

        return list_node
    
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
            return ListNode(None)
        
def main():
    s = Solution()

    head = s.listify([1,2,3,4])
    s.reorderList(head)
    print('head = [1,2,3,4]:', s.printListNode(head))
    head = s.listify([1,2,3,4,5])
    s.reorderList(head)
    print('head = [1,2,3,4,5]:', s.printListNode(head))

if __name__ == '__main__':
    main()