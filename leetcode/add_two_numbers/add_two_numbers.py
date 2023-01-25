from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __get_number(self, head: Optional[ListNode]) -> int:
        numbers = []
        while head:
            numbers.append(str(head.val))
            head = head.next
        return int(''.join(numbers[::-1]))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = list(map(int, list(str(self.__get_number(l1) + self.__get_number(l2)))))
        result = ListNode()

        for i, number in enumerate(sum):
            if i == 0:
                result.next = None
                result.val = number
            else:
                result.next = ListNode(result.val, result.next)
                result.val = number
        return result

    def get_list(self, head: Optional[ListNode]):
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        return head_list

def main():
    s = Solution()
    print('l1 = [2,4,3], l2 = [5,6,4]:', s.get_list(s.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))))
    print('l1 = [0], l2 = [0]:', s.get_list(s.addTwoNumbers(ListNode(0), ListNode(0))))
    print('l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]:', s.get_list(s.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))

if __name__ == '__main__':
    main()