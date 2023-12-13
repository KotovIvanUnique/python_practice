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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            result_list = None

            for i in range (len(lists) - 1):
                result_list = self.mergeTwoLists(lists[i] if result_list is None else result_list, lists[i + 1])

            return result_list             
    
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

    print('lists = [[1,4,5],[1,3,4],[2,6]]:', s.printListNode(s.mergeKLists(lists = [s.listify([1,4,5]),s.listify([1,3,4]),s.listify([2,6])])))
    print('lists = []:', s.printListNode(s.mergeKLists(lists = [])))
    print('lists = [[]]:', s.printListNode(s.mergeKLists(lists = [[]])))

if __name__ == '__main__':
    main()