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
        
def main():
    s = Solution()
    # print('head = [1,2,3,4,5]:', s.reverseList(head = [1,2,3,4,5]))
    # print('head = [1,2]:', s.reverseList(head = [1,2]))
    # print('head = []:', s.reverseList(head = []))
    print('head = [1,2,3,4,5]:', s.printListNode(s.reverseList(head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))))))
    print('head = [1,2]:', s.printListNode(s.reverseList(head = ListNode(1,ListNode(2)))))
    print('head = []:', s.printListNode(s.reverseList(head = ListNode(None))))  

if __name__ == '__main__':
    main()