from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = merged_curr = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                merged_curr.next = list1
                list1 = list1.next
            else:
                merged_curr.next = list2
                list2 = list2.next
            merged_curr = merged_curr.next
        
        merged_curr.next = list1 or list2

        return merged.next
    
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

    print('list1 = [1,2,4], list2 = [1,3,4]:', s.printListNode(s.mergeTwoLists(list1 = s.listify([1,2,4]), list2 = s.listify([1,3,4]))))
    print('list1 = [], list2 = []:', s.printListNode(s.mergeTwoLists(list1 = s.listify([]), list2 = s.listify([]))))
    print('list1 = [], list2 = [0]:', s.printListNode(s.mergeTwoLists(list1 = s.listify([]), list2 = s.listify([0]))))

if __name__ == '__main__':
    main()