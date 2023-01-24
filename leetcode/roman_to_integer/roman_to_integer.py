class Solution:
    def __init__(self):
        self.__mapping = {'I': 1,
                          'V': 5,
                          'X': 10,
                          'L': 50,
                          'C': 100,
                          'D': 500,
                          'M': 1000,}

    def __is_substract(self, letter: str, next_letter: str):
        if letter == 'I' and next_letter in ['V', 'X']:
            return True
        elif letter == 'X' and next_letter in ['L', 'C']:
            return True
        elif letter == 'C' and next_letter in ['D', 'M']:
            return True
        else:
            return False

    def romanToInt(self, s: str) -> int:
        s = list(s)
        length = len(s)
        result = 0

        for i in range(length):
            if i < length-1 and self.__is_substract(s[i], s[i+1]):
                continue
            elif i > 0 and self.__is_substract(s[i-1], s[i]):
                result += self.__mapping[s[i]] - self.__mapping[s[i-1]]
            else:
                result += self.__mapping[s[i]]

        return result

def main():
    s = Solution()

    print('III = ', s.romanToInt('III'))
    print('LVIII = ', s.romanToInt('LVIII'))
    print('MCMXCIV = ', s.romanToInt('MCMXCIV'))

if __name__ == '__main__':
    main()