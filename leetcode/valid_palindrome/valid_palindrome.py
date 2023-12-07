from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i].lower(), s[j].lower()
            if a.isalnum() and b.isalnum():
                if a != b: return False
                else:
                    i, j = i + 1, j - 1
                    continue
            i, j = i + (not a.isalnum()), j - (not b.isalnum())
        return True

def main():
    s = Solution()
    print('s = "A man, a plan, a canal: Panama"', s.isPalindrome(s = "A man, a plan, a canal: Panama"))
    print('s = "race a car"', s.isPalindrome(s = "race a car"))
    print('s = " "', s.isPalindrome(s = " "))

if __name__ == '__main__':
    main()