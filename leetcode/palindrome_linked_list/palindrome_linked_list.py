class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __get_reversed_head(self, head: ListNode) -> ListNode:
        reversed = ListNode()
        while head:
            next = head.next
            if next:
                reversed.val, reversed.next = next, ListNode(head.val, reversed.next)
            else:
                reversed = ListNode(head.val, reversed.next)
            head = next
        return reversed

    def isPalindrome(self, head: ListNode) -> bool:
        reversed = self.__get_reversed_head(head)
        while head:
            if head.val == reversed.val:
                head = head.next
                reversed = reversed.next
            else:
                return False
        return True

def main():
    s = Solution()
    print('[1, 2, 2, 1]:', s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
    print('[1, 2]:', s.isPalindrome(ListNode(1, ListNode(2))))
    print('[1, 1, 2, 1]:', s.isPalindrome(ListNode(1, ListNode(1, ListNode(2, ListNode(1))))))


if __name__ == '__main__':
    main()