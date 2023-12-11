from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        
        if not head:
            return None
        
        while head.next:
            reversed = ListNode(head.val, reversed)
            head = head.next

        return ListNode(head.val, reversed)
    
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
    # print('head = [1,2,3,4,5]:', s.reverseList(head = [1,2,3,4,5]))
    # print('head = [1,2]:', s.reverseList(head = [1,2]))
    # print('head = []:', s.reverseList(head = []))
    print('head = [1,2,3,4,5]:', s.printListNode(s.reverseList(head = s.listify([1,2,3,4,5]))))
    print('head = [1,2]:', s.printListNode(s.reverseList(head = s.listify([1,2]))))
    print('head = []:', s.printListNode(s.reverseList(head = s.listify([]))))  

if __name__ == '__main__':
    main()