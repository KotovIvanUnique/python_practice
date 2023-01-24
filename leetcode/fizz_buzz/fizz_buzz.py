class Solution:
    def __get_string(self, i: int) -> str:
        if i%3 == 0 and i%5 == 0:
            return 'FizzBuzz'
        elif i%3 == 0:
            return 'Fizz'
        elif i%5 == 0:
            return 'Buzz'
        else:
            return str(i) 

    def fizzBuzz(self, n: int) -> list:
        return [self.__get_string(i) for i in range(1, n+1)]

def main():
    s = Solution()
    print('3:', s.fizzBuzz(3))
    print('5:', s.fizzBuzz(5))
    print('15:', s.fizzBuzz(15))

if __name__ == '__main__':
    main()