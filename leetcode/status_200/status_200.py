from collections import Counter

class Solution:
    def get_sum(self, s) -> int:
        res = 0
        while s > 0:
            res += s
            s -= 1
        return res

    def get_number_of_good_pairs(self, n, numbers) -> int:
        n = int(n)
        numbers = list(map(int, numbers.split()))

        if n < 2:
            return 0
        else:
            return sum([self.get_sum(x - 1) for x in Counter([x % 200 for x in numbers]).values()])

def main():
    s = Solution()

    print('n = 5, pairs = 203 404 204 200 403', s.get_number_of_good_pairs('5', '203 404 204 200 403'))
    print('n = 1, pairs = 1000000', s.get_number_of_good_pairs('1', '1000000'))
    print('n = 3, pairs = 2022 2020 2021', s.get_number_of_good_pairs('3', '2022 2020 2021'))

if __name__ == '__main__':
    main()