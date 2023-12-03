from typing import List

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        try:
            self.array[self.length] = n
            self.length += 1

        except IndexError:
            self.resize()
            self.array[self.length] = n
            self.length += 1

    def popback(self) -> int:
        last_element = self.array[self.length - 1]

        if self.length > 0:
            self.length -= 1

        return last_element

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity

        for i in range(len(self.array)):
            new_array[i] = self.array[i]

        self.array = new_array

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
        
def main():
    s = DynamicArray(2)

if __name__ == '__main__':
    main()