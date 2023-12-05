from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = dict()
        t_hash = dict()

        for i in s:
            s_hash[i] = s_hash.get(i, 0) + 1

        for i in t:
            t_hash[i] = t_hash.get(i, 0) + 1 

        if s_hash == t_hash:
            return True
        else:
            return False

def main():
    s = Solution()
    print(':', s.isAnagram('1234', '4321'))
    print(':', s.isAnagram('1221', '3'))

if __name__ == '__main__':
    main()