class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        palindrome = []

        while head:
            palindrome.append(head.val)
            head = head.next

        if palindrome == palindrome[::-1]:
            return True
        else:
            return False

def main():
    s = Solution()
    print('[1, 2, 2, 1]:', s.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
    print('[1, 2]:', s.isPalindrome(ListNode(1, ListNode(2))))


if __name__ == '__main__':
    main()