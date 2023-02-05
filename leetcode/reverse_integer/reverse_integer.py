class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        x = int(x[::-1]) if x[0] != '-' else int('-'+x[:0:-1])
        if x > -2**31 and x < (2**31)-1:
            return x
        else:
            return 0

def main():
    s = Solution()
    print('123:', s.reverse(123))
    print('-123:', s.reverse(-123))
    print('120:', s.reverse(120))

if __name__ == '__main__':
    main()