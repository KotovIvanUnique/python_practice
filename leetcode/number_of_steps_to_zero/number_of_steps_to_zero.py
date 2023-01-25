class Solution:
    def __is_even(self, num: int) -> bool:
        if num%2 == 0:
            return True
        else:
            return False

    def __get_next_number(self, num: int) -> int:
        if self.__is_even(num):
            return num/2
        else:
            return num-1

    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            num = self.__get_next_number(num)
            steps += 1
        return steps

def main():
    s = Solution()
    print('14:', s.numberOfSteps(14))
    print('8:', s.numberOfSteps(8))
    print('123:', s.numberOfSteps(123))

if __name__ == '__main__':
    main()