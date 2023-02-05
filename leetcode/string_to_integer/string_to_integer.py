class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign, res, i = 1, 0, 0
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
        res = max(min(res * sign, 2**31 - 1), -2**31)
        return res

def main():
    s = Solution()
    print('42:', s.myAtoi('42'))
    print('   -42:', s.myAtoi('   -42'))
    print('4193 with words:', s.myAtoi('4193 with words'))
    print("words and 987:", s.myAtoi('words and 987'))
    print("+-12:", s.myAtoi("+-12"))
    print(":", s.myAtoi(""))
    print("+:", s.myAtoi("+"))
    print("00000-42a1234:", s.myAtoi("00000-42a1234"))
    print("3.14159:", s.myAtoi("3.14159"))
    print("  -0012a42:", s.myAtoi("  -0012a42"))

if __name__ == '__main__':
    main()