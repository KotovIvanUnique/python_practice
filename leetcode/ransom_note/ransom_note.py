class Solution:
    def __count_letters(self, string: str) -> dict:
        letter_counter = {}
        for letter in list(string):
            if letter not in letter_counter.keys():
                letter_counter[letter] = 1
            else:
                letter_counter[letter] = letter_counter.get(letter) + 1
        return letter_counter

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_counter = self.__count_letters(ransomNote)
        magazine_counter = self.__count_letters(magazine)
        
        for key, value in ransomNote_counter.items():
            if value <= magazine_counter.get(key, 0):
                continue
            else:
                return False
        return True

def main():
    s = Solution()
    print('a, b:', s.canConstruct('a', 'b'))
    print('aa, ab:', s.canConstruct('aa', 'ab'))
    print('aa, aab:', s.canConstruct('aa', 'aab'))

if __name__ == '__main__':
    main()