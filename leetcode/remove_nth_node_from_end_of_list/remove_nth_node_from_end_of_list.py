from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None

        counter = 1
        curr = head

        while curr.next:
            counter += 1
            curr = curr.next

        prev = None
        curr = head
        while counter - n > 0:
            prev = curr
            curr = curr.next
            counter -= 1
        
        if prev:
            prev.next = curr.next
        else:
            return curr.next

        return head
        
    
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

    print('head = [1,2,3,4,5], n = 2:', s.printListNode(s.removeNthFromEnd(head = s.listify([1,2,3,4,5]), n = 2)))
    print('head = [1], n = 1:', s.printListNode(s.removeNthFromEnd(head = s.listify([1]), n = 1)))
    print('head = [1,2], n = 1:', s.printListNode(s.removeNthFromEnd(head = s.listify([1,2]), n = 1)))
    print('head = [1,2], n = 2:', s.printListNode(s.removeNthFromEnd(head = s.listify([1,2]), n = 2)))

if __name__ == '__main__':
    main()