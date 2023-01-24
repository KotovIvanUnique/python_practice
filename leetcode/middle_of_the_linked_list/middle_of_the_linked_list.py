from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __count_nodes(self, head: Optional[ListNode]) -> int:
        i = 0
        while head:
            head = head.next
            i += 1
        return i

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = self.__count_nodes(head)
        middle = count//2 + 1
        i = 1
        result = ListNode()

        while head:
            if i == middle:
                result = ListNode(head.val, head.next)
                return result
            else:
                head = head.next
                i += 1

    def get_list(self, head: Optional[ListNode]):
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        return head_list
        

def main():
    s = Solution()
    print('[1,2,3,4,5]:', s.get_list(s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))))
    print('[1,2,3,4,5,6]:', s.get_list(s.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))))

if __name__ == '__main__':
    main()